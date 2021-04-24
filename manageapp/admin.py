from django.contrib import admin
from .models import guard_reg
from .models import user_reg
from .models import rent
from .models import maintain
from .models import addevent
from .models import complain
from .models import guest
from .models import Message
from .models import SendRecieve
# Register your models here.
admin.site.register(guard_reg)
admin.site.register(user_reg)
admin.site.register(rent)
admin.site.register(addevent)
admin.site.register(maintain)
admin.site.register(complain)
admin.site.register(guest)
admin.site.register(Message)
admin.site.register(SendRecieve)