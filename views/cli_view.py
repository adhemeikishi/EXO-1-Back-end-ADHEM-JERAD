class CLIView:
    """Vue CLI (interface utilisateur en ligne de commande)."""

    @staticmethod
    def display_tasks(tasks):
        if not tasks:
            print("\n📭 Aucune tâche pour le moment.\n")
            return
        print("\n📋 Liste des tâches :")
        for task in tasks:
            print(f" - {task}")
        print()

    @staticmethod
    def display_message(message: str):
        print(f"\n💬 {message}\n")

    @staticmethod
    def display_help():
        print("""
🧰 Commandes disponibles :
  add <titre> [description]   → Ajouter une tâche
  list                        → Afficher toutes les tâches
  done <id>                   → Marquer une tâche comme terminée
  delete <id>                 → Supprimer une tâche
  help                        → Afficher l'aide
  exit                        → Quitter le programme
""")
