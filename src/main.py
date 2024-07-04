from textual.app import App, ComposeResult
from textual.containers import Horizontal, ScrollableContainer
from textual.reactive import reactive
from textual.widgets import Button, Header, Footer, Static, Placeholder, Tab, TabPane, Tabs, TabbedContent




class I3Display(Static):

    def __init__(self):
        Static.__init__(self)

    def compose(self) -> ComposeResult:
        yield ScrollableContainer(Placeholder(label="hello from i3"))


class PolybarDisplay(Static):

    def __init__(self):
        Static.__init__(self)

    def compose(self) -> ComposeResult:

        yield ScrollableContainer(Placeholder(label="hello from polybar"))


class DmenuDisplay(Static):

    def __init__(self):
        Static.__init__(self)

    def compose(self) -> ComposeResult:
        yield ScrollableContainer(Placeholder(label="hello from Dmenu"))


class ctrlpnl(App):


    CSS_PATH = "ctrlpnl.css"
    BINDINGS = [
            ("D", "close_program", "Close Application")
    ]
    def compose(self) -> ComposeResult:
        yield Footer()
        with TabbedContent(initial="i3"):
            with TabPane("i3 Settings", id="i3"):
                yield I3Display()
            with TabPane("Polybar Settings", id="polybar"):
                yield PolybarDisplay()
            with TabPane("dmenu Settings", id="dmenu"):
                yield DmenuDisplay()

    def action_show_tab(self, tab: str) -> None:
        """Switch to a new tab."""
        self.get_child_by_type(TabbedContent).active = tab

    def on_mount(self) -> None:
        self.screen.styles.background = "transparent"
    
    def action_close_program(self) -> None:
        exit()


if __name__ == "__main__":
    app = ctrlpnl()
    app.run()
