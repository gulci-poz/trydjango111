from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self):
        context = super(HomeView, self).get_context_data()
        context['title'] = 'home page'
        return context


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self):
        context = super(AboutView, self).get_context_data()
        context['title'] = 'about'
        return context


class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self):
        context = super(ContactView, self).get_context_data()
        context['title'] = 'contact'
        return context
