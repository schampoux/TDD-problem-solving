from rich.console import Console
from rich.traceback import install
import unittest
from rich.style import Style
from rich.color import Color

install()  # Enable rich traceback formatting

console = Console()

# Custom color styles
FAIL_STYLE = Style(color="red", bold=True)
ERROR_STYLE = Style(color="yellow", bold=True)
PASS_STYLE = Style(color="green", bold=True)
TEST_NAME_STYLE = Style(color="yellow", bold=True)  # Test name in yellow
ASSERTION_ERROR_STYLE = Style(color="cyan", bold=True)  # Assertion errors in cyan

def run_tests():
    loader = unittest.TestLoader()
    suite = loader.discover("tests", pattern="test_*.py")  # Adjust the pattern if needed

    print(f"Discovered tests: {suite}")  # Debug print

    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    # Print summary with custom colors
    console.print(f"\n[bold green]Tests run: {result.testsRun}[/bold green]")

    # Handle failures with color
    if result.failures:
        console.print(f"[bold red]Failures: {len(result.failures)}[/bold red]")
        for test, err in result.failures:
            test_name = test.id().split('.')[-1]  # Extract the test name
            console.print(f"[yellow]FAIL: {test_name}[/yellow]")  # Test name in yellow

            # Color the assertion error in cyan
            console.print(f"[cyan]Assertion Error:[/cyan] {err}", style=ASSERTION_ERROR_STYLE)
    
    # Handle errors (non-assertion failures)
    if result.errors:
        console.print(f"[bold yellow]Errors: {len(result.errors)}[/bold yellow]")
        for test, err in result.errors:
            test_name = test.id().split('.')[-1]  # Extract the test name
            console.print(f"[yellow]ERROR: {test_name}[/yellow]")  # Test name in yellow

            console.print(f"[cyan]Error Message:[/cyan] {err}", style=ERROR_STYLE)

    # Handle passed tests
    if result.testsRun > len(result.failures) + len(result.errors):
        console.print(f"[bold green]Passed: {result.testsRun - len(result.failures) - len(result.errors)}[/bold green]")

if __name__ == "__main__":
    run_tests()

