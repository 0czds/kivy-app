from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class SimpleApp(App):
    def build(self):
        # تخطيط عمودي لعناصر الشاشة
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        # عنصر نصي
        self.label = Label(text='مرحباً بك في تطبيق بايثون!', font_size=24)
        
        # زر تفاعلي
        button = Button(text="Click here", font_size=20, size_hint=(1, 0.3))
        button.bind(on_press=self.on_button_click)
        
        # إضافة العناصر إلى التخطيط
        layout.add_widget(self.label)
        layout.add_widget(button)
        
        return layout

    def on_button_click(self, instance):
        self.label.text = "Clicked!"

if __name__ == '__main__':
    SimpleApp().run()
