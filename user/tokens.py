from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six

# PasswordResetTokenGenerator is generating a token without persisting it in the database so,
# we extended it to create a unique token generator to confirm registration or email address.
# This make use of your project’s SECRET_KEY, so it is a secure and reliable method.


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.profile.signup_confirmation)
        )


account_activation_token = AccountActivationTokenGenerator()
