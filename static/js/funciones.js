/*============================================
 * FUNCION DE VALIDACION DEL FORMULARIO LOGIN
 *============================================*/

$(document).ready(function() {
    $('.form_login').bootstrapValidator({
        //message: 'Este valor no es válido',
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            usuario: {
                //message: 'El usuario no es válido',
                validators: {
                    notEmpty: {
                        //message: 'Este campo no debe estas vacío'
                    },
                    stringLength: {
                        min: 7,
                        //max: 9,
                        //message: 'The username must be more than 6 and less than 30 characters long'
                    },
                    integer: {
                    },
                    regexp: {
                        regexp: /^[0-9_\.\-]+$/,
                        //message: 'The username can only consist of alphabetical, number and underscore'
                    }
                }
            },
            password: {
                //message: 'El usuario no es válido',
                validators: {
                    notEmpty: {
                        //message: 'Este campo no debe estas vacío'
                    },
                    stringLength: {
                        min: 8,
                        //max: 30,
                        //message: 'The username must be more than 6 and less than 30 characters long'
                    },
                    regexp: {
                        regexp: /^(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z])./,
                        //message: 'The username can only consist of alphabetical, number and underscore'
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
