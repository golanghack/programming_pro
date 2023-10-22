# Import HappyX
import happyx


# Declare component
component TodoItem:
  checked: bool = false 
  # Declare HTML template
  `template`:
    if self.checked:
      tDiv(class="flex items-center bg-green-200 rounded-md px-4 py-1 cursor-pointer select-none"):
        slot
        @click:
          self.checked = not self.checked
    else:
      tDiv(class = "flex items-center bg-red-200 rounded-md px-4 py-1 cursor-pointer select-none"):
        slot
        @click:
          self.checked = not self.checked

  `script`:
    echo "Start coding!"
