class TemplateManagementEngine:
    """A class to manage email templates."""

    def __init__(self):
        otp_template = None
        # Example of templates stored in memory (you can replace this with a DB or file storage)
        self.templates = {
            'OTP_TEMPLATE': {otp_template},
        }

    def get_template_by_code(self, template_code, corporate_name):
        """Fetch template by its code and replace corporate-specific placeholders."""
        template = self.templates.get(template_code)
        if template:
            # Replace corporate_name in the subject and body
            template['subject'] = template['subject'].replace('[corporate_name]', corporate_name)
            template['body'] = template['body'].replace('[corporate_name]', corporate_name)
            return template
        return None

    def replace_tags(self, template_string, **kwargs):
        """Replace all occurrences of replace tags in the template string with the passed arguments."""
        try:
            for k, v in kwargs.items():
                template_string = template_string.replace(f'[{k}]', str(v))
            return template_string
        except Exception as e:
            print(f"Error replacing tags: {e}")
            return template_string