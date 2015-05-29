/*============================================
 * FUNCION DE VALIDACION DEL FORMULARIO LOGIN
 *============================================*/
$(document).ready(function() {
    $('.form_login').bootstrapValidator({
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            usuario: {
                validators: {
                    notEmpty: {
                    },
                    stringLength: {
                        min: 7,
                    },
                    regexp: {
                        regexp: /^[0-9_\.\-]+$/,
                    }
                }
            },
            password: {
                validators: {
                    notEmpty: {
                    },
                    stringLength: {
                        min: 8,
                    },
                    regexp: {
                        regexp: /^(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z])./,
                    }
                }
            }
            
        }
    });
});

/*=========================================================
 *FUNCION DE VALIDACION DEL FORMULARIO RECUPERAR CONTRASEÑA
 *=========================================================*/

$(document).ready(function() {
    $('.form-recuperarPassword').bootstrapValidator({
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            email: {
                validators: {
                    notEmpty: {
                    },
                    emailAddress: {
                    },
                }
            }
        }
    });
});

/*=========================================================
 *FUNCION DE VALIDACION DEL FORMULARIO CAMBIAR CONTRASEÑA
 *=========================================================*/

$(document).ready(function() {
    $('.form_changePass').bootstrapValidator({
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            password_actual: {
                validators: {
                    notEmpty: {
                    },
                    stringLength: {
                        min: 8,
                    },
                    regexp: {
                        regexp: /^(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z])./,
                    }
                }
            },
            nuevo_password: {
                validators: {
                    notEmpty: {
                    },
                    stringLength: {
                        min: 8,
                    },
                    regexp: {
                        regexp: /^(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z])./,
                    },
                    identical: {
                        field: 'repetir_password',
                    }
                }
            },
            repetir_password: {
                validators: {
                    notEmpty: {
                    },
                    stringLength: {
                        min: 8,
                    },
                    regexp: {
                        regexp: /^(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z])./,
                    },
                    identical: {
                        field: 'nuevo_password',
                        message: 'Las contraseñas no son iguales'
                    }
                }
            },
        }
    });
});


/*=========================================
 * FUNCIONES DEL TECLADO PARA INGRESAR PIL
 *=========================================*/

//MUESTRA Y OCULTA EL DIV QUE CONTIENE EL TECLADO
$(document).ready(function(){
  $(".mostrar").click(function(){
    $(".teclado").show();
  });
  $(".cerrar").click(function(){
    $(".teclado").hide();
  });
});

//BLOQUEA EL TECLADO FISICO
$(document).ready(function () {
  $(".block").keypress(function(e) {
    if (e.which) {
      return false;
    }
  });
});

$(document).ready(function(){
    //MUESTRA EN PANTALLA LA TECLA PRESIONADA
    $(".val").click(function(e){
         e.preventDefault();
          var a = $(this).attr("href");
          $(".salida").val($(".salida").val() + a);
    });

    //LIMPIA TODA LA PANTALLA 
    $(".clear").click(function(){
          $(".salida").val("");
    });

    //BORRA LA PANTALLA CON UN BACKSPACE PERO NO FUNCIONA
    $(".back").click(function(){
    });
});

$(document).ready(function(){
    $(".modal_error").modal('toggle');
});
$(document).ready(function(){
    $('#table').dataTable( {
          "aaSorting": [[ 1, "desc" ]]
    } );
});


/*==================================
 * FUNCION DE DATEPICKER
 *==================================*/
$(document).ready(function() {
    $('#datePicker')
        .datepicker({
            format: 'dd/mm/yyyy'
        })
        .on('changeDate', function(e) {
            // Revalidate the date field
            $('#eventForm').bootstrapValidator('revalidateField', 'date');
        });

    $('#eventForm').bootstrapValidator({
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            name: {
                validators: {
                    notEmpty: {
                        message: 'The name is required'
                    }
                }
            },
            date: {
                validators: {
                    notEmpty: {
                        message: 'The date is required'
                    },
                    date: {
                        format: 'MM/DD/YYYY',
                        message: 'The date is not a valid'
                    }
                }
            }
        }
    });
});

$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

$(document).ready(function(){
    $('#verificar').click(function(){
        $('#error-documento').remove();
        documento = $('#id_username');
        if(documento.val()==''){
            $('#div-documento').append('<br><div id ="error-documento" class="alert alert-danger alert-dismissible" role="alert">'+
            '<button type="button" class="close" data-dismiss="alert"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>'+
            '<strong> Debe ingresar el numero de documento </strong></div>');
        }else{
            toLoad = '../obtener_persona/'+documento.val()+'/';
            $.get(toLoad,function(data){
                if(data.length > 0){
                    for(var i = 0; i < data.length; i++){
                        $('#id_last_name').removeAttr('disabled');
                        $('#id_last_name').val(data[i].fields["apellidos"]);
                        $('#id_first_name').removeAttr('disabled');
                        $('#id_first_name').val(data[i].fields["nombres"]);
                        $('#id_email').removeAttr('disabled');
                        $('#div-documento').append('<input type="hidden" id="persona_id" name="persona_id" value="'+data[i].fields["id"]+'"/>');
                        $('#verificar').attr('disabled','disabled');      
                    }
                }else{
                    $('#div-documento').append('<br><div id ="error-documento" class="alert alert-danger alert-dismissible" role="alert">'+
            '<button type="button" class="close" data-dismiss="alert"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>'+
            '<strong> La persona que busca no existe. </strong></div>');      
                    $('#id_last_name').attr('disabled','disabled');
                    $('#id_last_name').val("");
                    $('#id_first_name').attr('disabled','disabled');
                    $('#id_first_name').val("");
                    $('#id_email').attr('disabled','disabled');
                }
            },"json");
        }
    });
     $('.number_input').keypress(function(tecla) {
        if(tecla.charCode < 48 || tecla.charCode > 57) return false;
    });
});