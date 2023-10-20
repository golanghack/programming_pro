# Import HappyX
import
  happyx,
  components/[todo_app]

var tasks = remember @[
  "Написать статью на Хабре",
  "Поделиться ей с друзьями"
]


# Declare application with ID "app"
appRoutes("app"):
  "/":
    tDiv(class = "flex flex-col p-8 w-fit gap-2"):
      tDiv(class = "flex rounded-md bg-gray-200 gap-2"):
        tInput(id = "taskName", class = "px-2 bg-transparent", placeholder = "Напишите что-нибудь")
        tButton:
          "+"
          @click:
            var data = document.getElementById("taskName").value
            if ($data).len > 0:
              tasks->add($data)
              app.router()
      for task in tasks:
        # Component usage
        component TodoItem:
          {task}