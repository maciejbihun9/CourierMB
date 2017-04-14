import pdb


class Utils:

    @staticmethod
    def store_form_data(form):
        # data.append(form.cleaned_data['name_and_surname'])
        for key, value in form.clean_data.items():
            form.cleaned_data[key]
        pdb.set_trace()
        return 0