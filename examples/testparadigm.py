from taskontrol.plugins import templates

class Paradigm(templates.ParadigmMinimal):
    def __init__(self, parent=None):
        super().__init__(parent)

if __name__ == "__main__":
    (app, paradigm) = templates.paramgui.create_app(Paradigm)
