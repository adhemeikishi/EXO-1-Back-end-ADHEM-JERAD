# EXO-1-Back-end-ADHEM-JERAD
Objectif

Créer une petite API ToDoList en JavaScript avec le framework Express.
L’API permet d’ajouter, supprimer et afficher des tâches en suivant une structure MVC (Model - View - Controller).

Installer les dépendances :
npm install

Lancer le serveur :

En mode normal :
npm start

En mode développement :
npm run dev

Architecture du projet
api-todolist/
│
├── controllers/
│   └── taskController.js
│
├── models/
│   └── taskModel.js
│
├── routes/
│   └── taskRoutes.js
│
├── server.js
└── package.json

Endpoints de l’API
Méthode	Endpoint	Corps (JSON)	Description
GET	/tasks	—	Affiche toutes les tâches
POST	/tasks/add	{ "id": 1, "title": "Faire les courses" }	Ajoute une tâche
DELETE	/tasks/remove/:id	—	Supprime une tâche par son ID
Exemple de test (avec Postman ou Thunder Client)

Ajouter une tâche

POST http://localhost:3000/tasks/add
Body :
{
  "id": 1,
  "title": "Apprendre Express"
}


Afficher toutes les tâches

GET http://localhost:3000/tasks


Supprimer une tâche

DELETE http://localhost:3000/tasks/remove/1

Auteur
Adhem Jerad
Étudiant en développement web et applications

