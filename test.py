from rich import print
from rich.console import Console

def fast_compare_texts(original_text, typed_text):
    original_words = original_text.split()
    typed_words = typed_text.split()

    console = Console()

    correct_count = 0
    wrong_count = 0
    skipped_count = 0
    extra_count = 0

    i, j = 0, 0  # i -> original index, j -> typed index

    console.print("[bold]Comparison Result:[/bold]\n")

    while i < len(original_words) or j < len(typed_words):
        if j >= len(typed_words):  
            console.print(f"[red]{original_words[i]}[/red]", end=" ")  # Skipped word
            skipped_count += 1
            i += 1
        elif i >= len(original_words):  
            console.print(f"[yellow]{typed_words[j]}[/yellow]", end=" ")  # Extra word
            extra_count += 1
            j += 1
        elif typed_words[j] == original_words[i]:  
            console.print(f"[green]{typed_words[j]}[/green]", end=" ")  # Correct word
            correct_count += 1
            i += 1
            j += 1
        else:  
            console.print(f"[magenta]{typed_words[j]}[/magenta]", end=" ")  # Wrong word
            wrong_count += 1
            j += 1

    print("\n\n[bold]Final Statistics:[/bold]")
    print(f"✅ Correct Words: [green]{correct_count}[/green]")
    print(f"❌ Wrong Words: [magenta]{wrong_count}[/magenta]")
    print(f"🛑 Skipped Words: [red]{skipped_count}[/red]")
    print(f"⚠️ Extra Words: [yellow]{extra_count}[/yellow]")

# Example usage
original_text = "In free India rural"
typed_text = "s India hi hif kf oi free rural"

fast_compare_texts(original_text, typed_text)
from rich import print
from rich.console import Console

def fast_compare_texts(original_text, typed_text):
    original_words = original_text.split()
    typed_words = typed_text.split()

    console = Console()

    correct_count = 0
    wrong_count = 0
    skipped_count = 0
    extra_count = 0

    i, j = 0, 0  # i -> original index, j -> typed index

    console.print("[bold]Comparison Result:[/bold]\n")

    while i < len(original_words) or j < len(typed_words):
        if j >= len(typed_words):  
            console.print(f"[red]{original_words[i]}[/red]", end=" ")  # Skipped word
            skipped_count += 1
            i += 1
        elif i >= len(original_words):  
            console.print(f"[yellow]{typed_words[j]}[/yellow]", end=" ")  # Extra word
            extra_count += 1
            j += 1
        elif typed_words[j] == original_words[i]:  
            console.print(f"[green]{typed_words[j]}[/green]", end=" ")  # Correct word
            correct_count += 1
            i += 1
            j += 1
        else:  
            console.print(f"[magenta]{typed_words[j]}[/magenta]", end=" ")  # Wrong word
            wrong_count += 1
            j += 1

    print("\n\n[bold]Final Statistics:[/bold]")
    print(f"✅ Correct Words: [green]{correct_count}[/green]")
    print(f"❌ Wrong Words: [magenta]{wrong_count}[/magenta]")
    print(f"🛑 Skipped Words: [red]{skipped_count}[/red]")
    print(f"⚠️ Extra Words: [yellow]{extra_count}[/yellow]")

# Example usage
original_text = "In free India rural"
typed_text = "s India hi hif kf oi free rural"

fast_compare_texts(original_text, typed_text)
