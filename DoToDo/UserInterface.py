__author__ = 'group-4'

#text based user interface will be here
import npyscreen

class MainScreen(npyscreen.FormBaseNew):
    def create(self):
       self.choice = self.add(npyscreen.TitleText, name='Selection')
       self.text_l1 = self.add(npyscreen.FixedText,
                               editable=False,
                               value='1:Appointment 2:Deadline 3:Unbound')

    def while_editing(self, *args, **keywords):
        if self.choice.value == '1':
            self.parentApp.getForm('APPOINTMENT').value = 'Appointment'
            self.parentApp.switchForm('APPOINTMENT')
        elif self.choice.value == '2':
            self.parentApp.getForm('DEADLINE').value = 'Deadline'
            self.parentApp.switchForm('DEADLINE')
        elif self.choice.value == '3':
            self.parentApp.getForm('UNBOUND').value = 'Unbound'
            self.parentApp.switchForm('UNBOUND')
        else:
            if len(self.choice.value) > 0:
                npyscreen.notify_confirm('Invalid Selection!!', title='Error', editw=1)
                self.choice.value = None


class TaskDetail(npyscreen.ActionForm):
    def create(self):
        self.value = None
        self.title = self.add(npyscreen.TitleText, name='Title')
        self.desc = self.add(npyscreen.TitleText, name='Description')
        self.status = self.add(npyscreen.TitleSelectOne, name='Status',
                               max_height=2,
                               values=['Pending', 'Done'],
                               scroll_exit=True)

    def on_cancel(self):
        self.parentApp.switchFormPrevious()


class AppointmentDetail(TaskDetail):
    def create(self):
        super(AppointmentDetail, self).create()
        self.start_date = self.add(npyscreen.TitleDateCombo, name='Start date', hidden=True)
        self.start_hour = self.add(npyscreen.TitleSlider, name='  hour', out_of=24)
        self.start_minute = self.add(npyscreen.TitleSlider, name='  minute', out_of=60, step=15)
        self.end_date = self.add(npyscreen.TitleDateCombo, name='End date')
        self.end_hour = self.add(npyscreen.TitleSlider, name='  hour', out_of=24)
        self.end_minute = self.add(npyscreen.TitleSlider, name='  minute', out_of=60, step=15)
        
    def on_cancel(self):
        super(AppointmentDetail, self).on_cancel()


class DeadlineDetail(TaskDetail):
    def create(self):
        super(DeadlineDetail, self).create()
        self.by_date = self.add(npyscreen.TitleDateCombo, name='Due date')
        self.by_hour = self.add(npyscreen.TitleSlider, name='  hour', out_of=24)
        self.by_minute = self.add(npyscreen.TitleSlider, name='  minute', out_of=60, step=15)


class UnboundDetail(TaskDetail):
    def create(self):
        super(UnboundDetail, self).create()
        self.priority = self.add(npyscreen.TitleSelectOne, name='Priority',
                                 max_height=5,
                                 values=['1-Now', '2-Next', '3-Soon', '4-Later', '5-Someday'],
                                 scroll_exit=True)


class TextUI(npyscreen.NPSAppManaged):
    def onStart(self):
        npyscreen.setTheme(npyscreen.Themes.ElegantTheme)
        self.addForm("MAIN", MainScreen, name='DoToDo App')
        self.addForm("TASK", TaskDetail, name='Detail')
        self.addForm("APPOINTMENT", AppointmentDetail, name='Detail')
        self.addForm("DEADLINE", DeadlineDetail, name='Detail')
        self.addForm("UNBOUND", UnboundDetail, name='Detail')

if __name__ == '__main__':
   TestApp = TextUI().run()