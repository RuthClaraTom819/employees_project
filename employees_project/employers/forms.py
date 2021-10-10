from django import forms
from django.core.exceptions import ValidationError


class GreetingAdminForm(forms.ModelForm):

    def clean_csv_file(self):
        upload = self.cleaned_data['file']

        if upload:
            filename = upload.name
            if filename.endswith(settings.FILE_UPLOAD_TYPE):
                csv = pd.read_csv(upload.name)
                

                if csv.isnull().any()['employee_code']:
                    raise forms.ValidationError(u'Missing time value data')

                elif csv.isnull().any()['employee_code']:
                    raise forms.ValidationError(u'Missing amplitude value data')
                
                else:
                    return upload

        else:
            raise forms.ValidationError("Please upload a .csv extention files only")
        
        return upload
