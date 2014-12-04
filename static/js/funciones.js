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
