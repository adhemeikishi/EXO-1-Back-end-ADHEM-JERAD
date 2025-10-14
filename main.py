#!/usr/bin/env python3
import sys
from controllers.task_controller import TaskController
from views.cli_view import CLIView


def main():
    controller = TaskController()
    view = CLIView()

    view.display_help()

    while True:
        command = input("👉 Commande : ").strip().split(" ", 2)

        if not command or command[0] == "":
            continue

        action = command[0].lower()

        if action == "add":
            if len(command) < 2:
                view.display_message("⚠️ Veuillez fournir un titre.")
                continue
            title = command[1]
            description = command[2] if len(command) == 3 else ""
            task = controller.add_task(title, description)
            view.display_message(f"Tâche ajoutée : {task}")

        elif action == "list":
            view.display_tasks(controller.list_tasks())

        elif action == "done":
            if len(command) < 2:
                view.display_message("⚠️ Veuillez indiquer l'ID de la tâche.")
                continue
            task = controller.complete_task(command[1])
            view.display_message(f"Tâche terminée : {task}" if task else "❌ Tâche introuvable.")

        elif action == "delete":
            if len(command) < 2:
                view.display_message("⚠️ Veuillez indiquer l'ID de la tâche.")
                continue
            task = controller.delete_task(command[1])
            view.display_message(f"Tâche supprimée : {task}" if task else "❌ Tâche introuvable.")

        elif action == "help":
            view.display_help()

        elif action == "exit":
            view.display_message("👋 Au revoir !")
            sys.exit(0)

        else:
            view.display_message("❌ Commande inconnue. Tapez 'help' pour voir les options.")


if __name__ == "__main__":
    main()
