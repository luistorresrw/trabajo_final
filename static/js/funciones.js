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
/*
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
                        message: 'The email is required and cannot be empty'
                    },
                    emailAddress: {
                            message: 'The input is not a valid email address'
                    }
                }
            }
        }
    });    
});
*/

/*=========================================================
 * FUNCION QUE HACE APARECER EL TECLADO PARA INGRESAR PIL
 *=========================================================*/
$(function () {
    $('#pil').keypad();
    $('#pil').keypad();
});