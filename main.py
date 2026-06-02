import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class JournalApp(App):
    def build(self):
        # The main layout holding everything vertically
        self.main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # 1. Header Title
        title = Label(
            text="My Personal Journal", 
            size_hint_y=0.1, 
            font_size='24sp', 
            bold=True
        )
        self.main_layout.add_widget(title)
        
        # 2. History Area (Scrollable view of past entries)
        self.scroll_view = ScrollView(size_hint_y=0.4)
        self.history_label = Label(
            text="Loading past entries...", 
            size_hint_y=None, 
            halign='left', 
            valign='top'
        )
        # Keep text formatted correctly inside the scroll view
        self.history_label.bind(texture_size=self.history_label.setter('size'))
        self.scroll_view.add_widget(self.history_label)
        self.main_layout.add_widget(self.scroll_view)
        
        # 3. Input Text Box (Where you type your thoughts)
        self.txt_input = TextInput(
            hint_text="Write your thoughts here...", 
            size_hint_y=0.4, 
            multiline=True
        )
        self.main_layout.add_widget(self.txt_input)
        
        # 4. Save Button
        save_btn = Button(
            text="Save Entry", 
            size_hint_y=0.1, 
            background_color=(0.1, 0.6, 0.3, 1)
        )
        save_btn.bind(on_press=self.save_entry)
        self.main_layout.add_widget(save_btn)
        
        # Define where the text file will save on your phone
        self.file_path = "journal_entries.txt"
        self.load_entries()
        
        return self.main_layout

    def load_entries(self):
        """Loads previous entries from the file and displays them."""
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as file:
                content = file.read()
                self.history_label.text = content if content.strip() else "No entries yet. Start writing!"
        else:
            self.history_label.text = "No entries yet. Start writing!"

    def save_entry(self, instance):
        """Appends the text input into the journal file."""
        entry_text = self.txt_input.text.strip()
        
        if entry_text:
            # Format the text with dividers
            formatted_entry = f"\n--- New Entry ---\n{entry_text}\n"
            
            # Append to file
            with open(self.file_path, "a", encoding="utf-8") as file:
                file.write(formatted_entry)
                
            # Clear text box and refresh the log view
            self.txt_input.text = ""
            self.load_entries()

if __name__ == '__main__':
    JournalApp().run()
