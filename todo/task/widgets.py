from django import forms


class DatePickerWidget(forms.DateInput):
    template_name = 'widgets/picker_date.html'

    class Media:
        css = {
            'all': [
                '//code.jquery.com/ui/1.12.1/themes/smoothness/jquery-ui.css',
            ],
        }
        js = [
            '//code.jquery.com/jquery-2.2.4.min.js',
            '//code.jquery.com/ui/1.12.1/jquery-ui.min.js',
        ]
