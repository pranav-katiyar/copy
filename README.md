# copy

aws sts --assume-role-with-saml --role-arn arn:aws:iam::733341525147:role/trsw-sandbox-dev-power-user --principal-arn arn:aws:iam:: 733341525147:saml-provider/okta --no-verify-ssl --saml-assertion
