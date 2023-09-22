import sys

import tests.test_logica
from src.vista.InterfazEnForma import App_EnForma
from src.logica.Logica import Logica

if __name__ == '__main__':
    # Punto inicial de la aplicación

    logica = Logica()

    app = App_EnForma(sys.argv, logica)
    sys.exit(app.exec_())