import tkinter as tk
import CommandList as cmd

def GUI():
    root = tk.Tk()
    root.title("Proceess Reader")

    Command = ["Task List Command"]

    # Command Button Layout
    for i in Command:
        btn = tk.Button(
            root,
            text=i,
            command=lambda: [
                Output.delete("1.0", tk.END),
                Output.insert(
                    tk.END,
                    str(
                        getattr(
                            cmd.CommandList.TaskList(), "stdout", ""
                        )  # Safely extracts stdout or defaults to empty string
                    ),
                ),
            ],
            width=20,
        )
        btn.pack(pady=5, padx=10, fill="x")

    # Text widget
    Output = tk.Text(root, height=15, width=60)
    Output.pack(padx=10, pady=5, fill="both", expand=True)

    root.mainloop()


GUI()