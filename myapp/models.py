from django.db import models

class Owner(models.Model):
    owner_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Property(models.Model):
    property_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_status = models.BooleanField(default=True)  # True = Available, False = Full
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='properties')

    def __str__(self):
      
      
        return self.name
      

class Tenant(models.Model):
    tenant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Lease(models.Model):
    lease_id = models.AutoField(primary_key=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='leases')
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='leases')
    start_date = models.DateField()
    end_date = models.DateField()
    STATUS_CHOICES = [
        ('active', 'ใช้งาน'),
        ('completed', 'เสร็จสมบูรณ์'),
        ('canceled', 'ยกเลิก'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return f"{self.property.name} - {self.tenant.name}"

class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
