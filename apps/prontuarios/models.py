from django.db import models

class RefPaises(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(unique=True, max_length=45L )
    
    def save(self, force_insert=False, force_update=False):
        self.descripcion = self.descripcion.upper()
        super(RefPaises, self).save(force_insert, force_update)        

    def clean(self):
        self.descripcion = self.descripcion.upper()

    def __unicode__(self):
      return  u'%s' % (self.descripcion)  
      self.descripcion = self.descripcion.upper()
    
    class Meta: 
        ordering = ["descripcion"]
        db_table = 'ref_paises'
        verbose_name='Pais'

    
class RefProvincia(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=45L)
    pais = models.ForeignKey(RefPaises,on_delete=models.PROTECT)
    

    def __unicode__(self):
        return  u'%s' % (self.descripcion)
        self.descripcion = self.descripcion.upper()

    
    def save(self, force_insert=False, force_update=False):
        self.descripcion = self.descripcion.upper()
        super(RefProvincia, self).save(force_insert, force_update)

    def clean(self):
        self.descripcion = self.descripcion.upper()    
        
    class Meta:
        unique_together=('descripcion','pais',)
        db_table = 'ref_provincia'
        ordering = ["descripcion"]
        verbose_name='Provincia'

class RefCiudades(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=80L)
    provincia = models.ForeignKey('RefProvincia', blank=True,  null=True, on_delete=models.PROTECT)
    pais = models.ForeignKey('RefPaises', on_delete=models.PROTECT)
    lat= models.CharField(max_length=50,blank=True,null=True)
    longi= models.CharField(max_length=50,blank=True,null=True)

    def __unicode__(self):
        return  u'%s' %  (self.descripcion)
        self.descripcion = self.descripcion.upper()

    def save(self, force_insert=False, force_update=False):
        self.descripcion = self.descripcion.upper()
        super(RefCiudades, self).save(force_insert, force_update)

    class Meta:
        unique_together = ('pais','provincia','descripcion',)
        ordering = ["descripcion"]
        db_table = 'ref_ciudades'

class UnidadesRegionales(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=80L)
    ciudad = models.ForeignKey('RefCiudades',on_delete=models.PROTECT)
     
    def __unicode__(self):
        return u'%s' %  (self.descripcion)
        self.descripcion = self.descripcion.upper()
         
 
    def save(self, force_insert=False, force_update=False):
        self.descripcion = self.descripcion.upper()
        super(UnidadesRegionales, self).save(force_insert, force_update)
 
    class Meta:
        unique_together = ('descripcion','ciudad')
        ordering = ["descripcion"]
        db_table = 'unidades_regionales'
 
class Dependencias(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=80)
    unidades_regionales = models.ForeignKey('UnidadesRegionales', related_name="unidades", on_delete=models.PROTECT)
    ciudad = models.ForeignKey('RefCiudades',on_delete=models.PROTECT)
   
 
    def __unicode__(self):
        return u'%s' % (self.descripcion)
        self.descripcion = self.descripcion.upper()
 
    def save(self, force_insert=False, force_update= False):
        self.descripcion = self.descripcion.upper()
        super(Dependencias, self).save(force_insert,force_update)
 
    class Meta:
        unique_together = ('descripcion','unidades_regionales','ciudad')
        ordering = ["descripcion"]
        db_table = 'dependencias'

class RefSexo(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(unique=True, max_length=15 )

    def __unicode__(self):
        return u'%s' % (self.descripcion)
        self.descripcion = self.descripcion.upper()

    def save(self, force_insert=False, force_update= False):
        self.descripcion = self.descripcion.upper()
        super(RefSexo, self).save(force_insert,force_update)
    
    def clean(self):
       self.descripcion = self.descripcion.upper()
        

    class Meta:
        ordering = ['descripcion']
        db_table = 'ref_sexo'
        verbose_name='Sexo'


class RefEstadosciv(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.CharField(unique=True, max_length = 12)

    def __unicode__(self):
        return u'%s' % (self.descripcion)
        self.descripcion = self.descripcion.upper()
    
    def save(self, force_insert=False,force_update=False):
        self.descripcion = self.descripcion.upper()
        super(RefEstadosciv, self).save(force_insert,force_update)

    def clean(self):
        self.descripcion = self.descripcion.upper()

    class Meta:
        ordering = ['descripcion']
        db_table = 'ref_estadociv' 
        verbose_name='Estado Civil'

class RefOcupacion(models.Model):
    id = models.AutoField(primary_key= True)
    descripcion = models.CharField(max_length=80,unique = True)

    def __unicode__(self):
        return u'%s' % (self.descripcion)
        self.descripcion = self.descripcion.upper()

    def save(self, force_insert=False,force_update=False):
        self.descripcion = self.descripcion.upper()
        super(RefOcupacion, self).save(force_insert,force_update)

    def clean(self):
        self.descripcion = self.descripcion.upper()

    class Meta:
        ordering = ['descripcion']
        db_table = 'ref_ocupacion'
        verbose_name='Ocupacion'

class RefTipoDocumento(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.CharField(unique=True, max_length = 19)

    def __unicode__(self):
        return u'%s' % (self.descripcion)
        self.descripcion = self.descripcion.upper()
    
    def save(self, force_insert=False,force_update=False):
        self.descripcion = self.descripcion.upper()
        super(RefTipoDocumento, self).save(force_insert,force_update) 

    def clean(self):
        self.descripcion = self.descripcion.upper()   

    class Meta:
        ordering = ['descripcion']
        db_table = 'ref_tipodocumento'

class Personas(models.Model):
    id = models.AutoField(primary_key = True)
    apellidos = models.CharField(max_length = 100,verbose_name='apellidos')
    nombres = models.CharField(max_length = 150,verbose_name='nombres')
    tipo_doc = models.ForeignKey('RefTipoDocumento', verbose_name='tipo documento',on_delete = models.PROTECT)
    nro_doc = models.CharField(max_length=50,unique=True)
    ciudad_nac = models.ForeignKey('RefCiudades',  blank = True, null = True,related_name='ciudad_nac', on_delete = models.PROTECT)
    pais_nac =models.ForeignKey('RefPaises',  blank = True, null = True,related_name='pais_nac', on_delete = models.PROTECT)
    ciudad_res = models.ForeignKey('RefCiudades', blank = True, null = True,related_name='ciudad_res', on_delete = models.PROTECT)
    sexo_id =  models.ForeignKey('RefSexo', on_delete = models.PROTECT)
    ocupacion = models.ForeignKey('RefOcupacion',blank = True, null = True,on_delete = models.PROTECT)
    cuit = models.CharField(max_length=11,default=0,blank = True, null = True)
    celular = models.CharField(max_length= 13,blank = True, null = True)
    fecha_nac = models.DateField()
    estado_civil=models.ForeignKey('RefEstadosciv',blank = True, null = True,on_delete = models.PROTECT)
    alias = models.CharField(max_length=150,blank = True, null = True)
    

    def __unicode__(self):
        return u'%s %s' % (self.apellidos, self.nombres)
        self.apellidos = self.descripcion.upper()
        self.nombres = self.nombres.upper()
        
    def save(self, force_insert = False, force_update = False):
        self.apellidos = self.apellidos.upper()
        self.nombres = self.nombres.upper()
        super(Personas, self).save(force_insert, force_update)    

    def clean(self):   
        self.apellidos = self.apellidos.upper()
        self.nombres = self.nombres.upper()
        #self.tipo_doc = self.tipo_doc
        self.nro_doc = self.nro_doc
        self.ciudad_nac = self.ciudad_nac
        self.pais_nac = self.pais_nac
        self.ciudad_res = self.ciudad_res
        #self.sexo_id = self.sexo_id
        self.ocupacion = self.ocupacion
        self.cuit = self.cuit
        self.celular = self.celular
        self.fecha_nac = self.fecha_nac
        self.estado_civil = self.estado_civil
        self.alias = self.alias.upper()

    def clean_fecha_nac(self):
        dias_anio = 365
        fecha_ingresada = self.cleaned_data.get('fecha_nac')
        fecha_actual = datetime.date.today().years
        diferencia = (datetime.date.today() - self.fecha_ingresada).days
        if fecha_ingresada / 4 == 0 and fecha_ingresada != 100 or fecha_actual / 400 == 0:
            dias_anio += 1
        anios = str(int(diferencia / dias_anio))
        if anios < 18:
            return unicode('La persona ingresada es menor de edad')


    class Meta:
        unique_together=('tipo_doc','nro_doc','apellidos','nombres',)
        ordering = ['apellidos']
        db_table = 'personas'
        