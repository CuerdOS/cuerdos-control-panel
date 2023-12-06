import gi
import subprocess

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class PanelDeControl(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Panel de Control")
        self.set_default_size(400, 300)

        # Crear un contenedor de pestañas
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        # Agregar pestañas al cuaderno de notas
        self.crear_pestaña("System and Security", [("Firewall", "gufw"), ("Setup repositories", "sakura -e pkexec setup-repos"), ("Cleaning system", "bleachbit"), ("GUI Package manager", "bauh")])
        self.crear_pestaña("Internet and Wireless", [("Network connections", "nm-connection-editor"), ("Bluetooth adapters", "blueman-adapters"), ("Bluetooth devices", "blueman-manager")])
        self.crear_pestaña("Hardware and Sound", [("Setup print server", "sakura -e pkexec cups-switch"), ("Sound control", "pavucontrol")])
        self.crear_pestaña("Users and Groups", [("Manage users and groups", "users-admin")])
        self.crear_pestaña("Customization", [("Set appearance", "gnome-tweaks"), ("Sway configuration file", "gedit ~/.config/sway/config"), ("I3 configuration file", "gedit ~/.config/i3/config")])

    def crear_pestaña(self, nombre, comandos):
        # Crear una nueva categoría (Gtk.Box) para cada pestaña
        categoria = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        
        # Crear un cuadro de lista para la categoría
        lista = Gtk.ListBox()
        lista.set_selection_mode(Gtk.SelectionMode.NONE)

        # Agregar elementos a la lista
        for comando in comandos:
            lista.add(self.crear_elemento_lista(comando))

        # Crear una etiqueta para la categoría
        etiqueta = Gtk.Label(label=nombre)
        etiqueta.set_margin_top(10)
        etiqueta.set_margin_bottom(5)
        categoria.pack_start(etiqueta, False, False, 0)
        categoria.pack_start(lista, True, True, 0)

        # Agregar la nueva pestaña al cuaderno de notas
        self.notebook.append_page(categoria, Gtk.Label(label=nombre))

    def crear_elemento_lista(self, comando):
        # Crear una fila para la lista con el comando
        fila = Gtk.ListBoxRow()
        cuadro = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        fila.add(cuadro)

        # Crear una etiqueta con el nombre del comando
        etiqueta = Gtk.Label(label=comando[0])
        cuadro.pack_start(etiqueta, True, True, 0)

        # Crear un botón para Open el comando
        boton = Gtk.Button(label="Open")
        boton.connect("clicked", self.Open_comando, comando[1])
        cuadro.pack_start(boton, False, False, 0)

        return fila

    def Open_comando(self, boton, comando):
        # Open el comando asociado al botón
        subprocess.Popen(["/bin/bash", "-c", comando])

if __name__ == "__main__":
    ventana = PanelDeControl()
    ventana.connect("destroy", Gtk.main_quit)
    ventana.show_all()
    Gtk.main()

