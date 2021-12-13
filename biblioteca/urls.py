from django.conf.urls import url, include
from biblioteca.views import editor_create, editor_list, index_biblioteca, editor_edit, \
    editor_detail, editor_delete, autor_create, autor_list, autor_detail, autor_edit, \
    autor_delete, libro_create, libro_list, libro_detail, libro_edit, libro_delete, \
    EditorCreate, EditorList, EditorDetail, EditorUpdate, EditorDelete, \
    AutorCreate, AutorList, AutorDetail, AutorUpdate, AutorDelete, \
    LibroCreate, LbroList, LibroDetail, LbroUpdate, LibroDelete

urlpatterns = [
    url(r'^editor/nuevofuncion/$', editor_create, name="editor_crearfuncion"),
    url(r'^editor/listarfuncion/$', editor_list, name="editor_listarfuncion"),
    url(r'^editor/detallefuncion/(?P<id_editor>\d+)/$', editor_detail, name="editor_detallefuncion"),
    url(r'^editor/editarfuncion/(?P<id_editor>\d+)/$', editor_edit, name="editor_editarfuncion"),
    url(r'^editor/eliminarfuncion/(?P<id_editor>\d+)/$', editor_delete, name="editor_eliminarfuncion"),
    url(r'^autor/nuevofuncion/$', autor_create, name="autor_crearfuncion"),
    url(r'^autor/listarfuncion/$', autor_list, name="autor_listarfuncion"),
    url(r'^autor/detallefuncion/(?P<id_autor>\d+)/$', autor_detail, name="autor_detallefuncion"),
    url(r'^autor/editarfuncion/(?P<id_autor>\d+)/$', autor_edit, name="autor_editarfuncion"),
    url(r'^autor/eliminarfuncion/(?P<id_autor>\d+)/$', autor_delete, name="autor_eliminarfuncion"),
    url(r'^libro/nuevofuncion/$', libro_create, name="libro_crearfuncion"),
    url(r'^libro/listarfuncion/$', libro_list, name="libro_listarfuncion"),
    url(r'^libro/detallefuncion/(?P<id_libro>\d+)/$', libro_detail, name="libro_detallefuncion"),
    url(r'^libro/editarfuncion/(?P<id_libro>\d+)/$', libro_edit, name="libro_editarfuncion"),
    url(r'^libro/eliminarfuncion/(?P<id_libro>\d+)/$', libro_delete, name="libro_eliminarfuncion"),
    url(r'^editor/nuevoclase/$', EditorCreate.as_view(), name="editor_crearclase"),
    url(r'^editor/listarclase/$', EditorList.as_view(), name="editor_listarclase"),
    url(r'^editor/detalleclase/(?P<pk>\d+)/$', EditorDetail.as_view(), name="editor_detalleclase"),
    url(r'^editor/editarclase/(?P<pk>\d+)/$', EditorUpdate.as_view(), name="editor_editarclase"),
    url(r'^editor/eliminarclase/(?P<pk>\d+)/$', EditorDelete.as_view(), name="editor_eliminarclase"),
    url(r'^autor/nuevoclase/$', AutorCreate.as_view(), name="autor_crearclase"),
    url(r'^autor/listarclase/$', AutorList.as_view(), name="autor_listarclase"),
    url(r'^autor/detalleclase/(?P<pk>\d+)/$', AutorDetail.as_view(), name="autor_detalleclase"),
    url(r'^autor/editarclase/(?P<pk>\d+)/$', AutorUpdate.as_view(), name="autor_editarclase"),
    url(r'^autor/eliminarclase/(?P<pk>\d+)/$', AutorDelete.as_view(), name="autor_eliminarclase"),
    url(r'^libro/nuevoclase/$', LibroCreate.as_view(), name="libro_crearclase"),
    url(r'^libro/listarclase/$', LbroList.as_view(), name="libro_listarclase"),
    url(r'^libro/detalleclase/(?P<pk>\d+)/$', LibroDetail.as_view(), name="libro_detalleclase"),
    url(r'^libro/editarclase/(?P<pk>\d+)/$', LbroUpdate.as_view(), name="libro_editarclase"),
    url(r'^libro/eliminarclase/(?P<pk>\d+)/$', LibroDelete.as_view(), name="libro_eliminarclase"),
    url(r'^$', index_biblioteca, name='index'),
    ]