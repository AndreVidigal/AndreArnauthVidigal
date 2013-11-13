from django.conf.urls import patterns, include, url

import photoSorlApp.views
import paypal.standard.ipn.views
import auth.views
import andrearnauthvidigal.settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'andrearnauthvidigal.views.home', name='home'),
    # url(r'^andrearnauthvidigal/', include('andrearnauthvidigal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	url(r'^$', photoSorlApp.views.StartingPoint.as_view(), name='startingPoint',),
	   (r'^$', 'show_cart', {'template_name':'cart/cart.html'}, 'show_cart'),
	url(r'^gallery/$', 'photoSorlApp.views.gallery', name='gallery',),		
	url(r'^item_\d+/$', 'photoSorlApp.views.itemView', name='itemView',),
	url(r'^nav/$', photoSorlApp.views.nav, name='nav',),			
	url(r'^new/$', photoSorlApp.views.CreateNewItem.as_view(), name='new',),
	url(r'^login/$',    'auth.views.login_user', name='login',),        
	url(r'^logout/$',   'auth.views.logout_user',name='logout',),	
    url(r'^register/$', 'auth.views.register',  name='register',),	
	url(r'^show_cart$', 'cart.views.show_cart', {'template_name':'cart/cart.html'}, 'show_cart'),
	url(r'^LeadingLights/(?P<product_slug>[-\w]+)/$', photoSorlApp.views.show_product, name='leadinglights'),		
	url(r'^ipn/$', paypal.standard.ipn.views.ipn, name='ipn'),
	#(r'^product/(?P<product_slug>[-\w]+)/$', 'show_product', 
    #   {'template_name': 'catalog/product.html'}, 'catalog_product'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':  andrearnauthvidigal.settings.MEDIA_ROOT}),	
)
