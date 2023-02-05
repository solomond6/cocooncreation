from django.urls import include, re_path
from . import views

app_name = 'adminPortal'

urlpatterns = [
    
    re_path(r'^api/articles/$', views.ArticleView.as_view(), name='articles'),
    re_path(r'^api/categories/$', views.CategoryView.as_view(), name='categories'),
    re_path(r'^api/authors/$', views.AuthorView.as_view(), name='authors'),
    
    re_path(r'^$', views.index, name='index'),
    re_path(r'^ping/$', views.ping, name='ping'),
    re_path(r'^login/$', views.login, name='index'),
    re_path(r'^authview/$', views.authview, name='authview'),

    re_path(r'^categories/$', views.categoriesview, name='categories'),
    re_path(r'^newcategory/$', views.newCategory, name='newcategory'),
    re_path(r'^submitNewCategory/$', views.submitNewCategory, name='submitNewCategory'),
    re_path(r'^editcategory/(?P<id>[a-zA-Z0-9_]+?)/$', views.categoryEditView, name='editcategory'),
    re_path(r'^updateCategory/$', views.updateCategory, name='updateCategory'),

    re_path(r'^authors/$', views.authorsview, name='authors'),
    re_path(r'^newauthor/$', views.newAuthor, name='newauthor'),
    re_path(r'^submitNewAuthor/$', views.submitNewAuthor, name='submitNewAuthor'),
    re_path(r'^editauthor/(?P<id>[a-zA-Z0-9_]+?)/$', views.authorEditView, name='editauthor'),
    re_path(r'^updateAuthor/$', views.updateAuthor, name='updateAuthor'),

    re_path(r'^articles/$', views.articleview, name='articles'),
    re_path(r'^newarticle/$', views.newArticle, name='newarticle'),
    re_path(r'^submitNewArticle/$', views.submitNewArticle, name='submitNewArticle'),
    re_path(r'^editarticle/(?P<id>[a-zA-Z0-9_]+?)/$', views.articleEditView, name='editarticle'),
    re_path(r'^updateArticle/$', views.updateArticle, name='updateArticle'),
    # re_path(r'^editarticle/(?P<id>[a-zA-Z0-9_]+?)/$', views.articleEditView, name='editarticle')

    re_path(r'^logoutview/$', views.logoutview, name='logoutview'),

    # re_path(r'^accounts/loggedin/$', views.loggedin, name='loggedin'),
    # re_path(r'^accounts/invalid/$', views.invalid, name='invalid_login'),
    # re_path(r'^index$', views.index, name='index'),
    # re_path(r'^authview/$', views.authview, name='authview'),
    # re_path(r'^newDriversList/$', views.newDriversList, name='newDriversList'),
    # re_path(r'^approvedDriversList/$', views.approvedDriversList, name='approvedDriversList'),
    # re_path(r'^rejectedDriversList/$', views.rejectedDriversList, name='rejectedDriversList'),
    # re_path(r'^driverDetails/(?P<driverid>[a-zA-Z0-9_]+?)/$', views.driverDetails, name='viewDriverDetails'),
    # re_path(r'^approvedriver/$', views.approveDriver, name='approvedriver'),
    # re_path(r'^searchdriver/$', views.searchDriver, name='searchdriver'),
    # re_path(r'^verificationofficers/$', views.verificationOfficersList, name='verificationofficers'),
    # re_path(r'^newverificationofficers/$', views.newVerificationOfficer, name='newverificationofficers'),
    # re_path(r'^submitverificationofficer/$', views.submitVerificationOfficer, name='submitverificationofficer'),
    # re_path(r'^scheduledriververification/$', views.scheduleNewDriversList, name='scheduleverification'),
    # re_path(r'^scheduleguarantorverification/$', views.scheduleNewGuarantorsList, name='scheduleverification'),
    # re_path(r'^scheduleDriver/(?P<driverid>[a-zA-Z0-9_]+?)/$', views.scheduleDriver, name='scheduleDriver'),
    # re_path(r'^verification_officer_login/$', views.VerificationOfficerLogin.as_view(), name='verification_officer_login'),
    # re_path(r'^verification_officer_schedule/$', views.VerificationOfficerSchedules.as_view(), name='verification_officer_schedule'),
    # re_path(r'^submit_verification_results/$', views.VerificationResults.as_view(), name='submit_verification_results'),
    # re_path(r'^verification_officer_performance/$', views.VerificationOfficerPerformance.as_view(), name='verification_officer_performance'),
    # re_path(r'^verification_officer_login_form/$', views.VerificationOfficerFormLogin, name='submit_verification_results'),
    # re_path(r'^verification_officer_schedule_form/$', views.VerificationOfficerFormSchedules, name='verification_officer_schedule_form'),
    # re_path(r'^submit_verification_results_form/$', views.VerificationFormResults, name='submit_verification_results_form')

    # re_path(r'^guarantors/$', views.index, name='guarantors'),
    # re_path(r'^accesstoken/$', views.gettoken, name='gettoken'),
    # re_path(r'^send/guarantordoc/$', views.sendguarantordoc, name='sendguarantordoc'),
    # re_path(r'^generatepdf/$', views.html_to_pdf_view, name='guarantorpdf'),
    # re_path(r'^psearch/(?P<guarantorid>[a-zA-Z0-9_]+?)/$', views.html_to_pdf_view, name='psearch'),
]