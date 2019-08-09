def link_model_form_and_admin(model, form, admin):
    admin.form = form
    form.Meta.model = model

    def model_admin():
        return admin

    model.model_admin = model_admin
