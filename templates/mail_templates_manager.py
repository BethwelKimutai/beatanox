from pyexpat.errors import messages


class TemplateManagementEngine:
    def replace_tags(self, template_string, **kwargs):
        """
        Replaces all the occurrences of replace tags with the passed in arguments.
        @param template_string: The template string we are supposed to replace tags.
        @type template_string: str
        @param kwargs: The key->word arguments representing the tags in the string without []
        @return: The template string replaced accordingly.
        @rtype: str
        """
        try:
            for k, v in kwargs.items():
                template_string = template_string.replace('[%s]' % str(k), str(v))
            return template_string
        except Exception as e:
            print('replace_tags Exception: %s', e)
        return template_string

    def send_login_otp(self, **kwargs):

        message = """
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html lang="en">
  <head>
    <!-- Compiled with Bootstrap Email version: 1.5.1 --><meta http-equiv="x-ua-compatible" content="ie=edge">
    <meta name="x-apple-disable-message-reformatting">
    <meta name="format-detection" content="telephone=no, date=no, address=no, email=no">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your OTP Code</title>
    <style type="text/css">
      body,table,td{font-family:Helvetica,Arial,sans-serif !important}.ExternalClass{width:100%}.ExternalClass,.ExternalClass p,.ExternalClass span,.ExternalClass font,.ExternalClass td,.ExternalClass div{line-height:150%}a{text-decoration:none}*{color:inherit}a[x-apple-data-detectors],u+#body a,#MessageViewBody a{color:inherit;text-decoration:none;font-size:inherit;font-family:inherit;font-weight:inherit;line-height:inherit}img{-ms-interpolation-mode:bicubic}table:not([class^=s-]){font-family:Helvetica,Arial,sans-serif;mso-table-lspace:0pt;mso-table-rspace:0pt;border-spacing:0px;border-collapse:collapse}table:not([class^=s-]) td{border-spacing:0px;border-collapse:collapse}@media screen and (max-width: 600px){.w-full,.w-full>tbody>tr>td{width:100% !important}.p-4:not(table),.p-4:not(.btn)>tbody>tr>td,.p-4.btn td a{padding:16px !important}.pt-4:not(table),.pt-4:not(.btn)>tbody>tr>td,.pt-4.btn td a,.py-4:not(table),.py-4:not(.btn)>tbody>tr>td,.py-4.btn td a{padding-top:16px !important}.pb-4:not(table),.pb-4:not(.btn)>tbody>tr>td,.pb-4.btn td a,.py-4:not(table),.py-4:not(.btn)>tbody>tr>td,.py-4.btn td a{padding-bottom:16px !important}.pt-6:not(table),.pt-6:not(.btn)>tbody>tr>td,.pt-6.btn td a,.py-6:not(table),.py-6:not(.btn)>tbody>tr>td,.py-6.btn td a{padding-top:24px !important}.pb-6:not(table),.pb-6:not(.btn)>tbody>tr>td,.pb-6.btn td a,.py-6:not(table),.py-6:not(.btn)>tbody>tr>td,.py-6.btn td a{padding-bottom:24px !important}.p-8:not(table),.p-8:not(.btn)>tbody>tr>td,.p-8.btn td a{padding:32px !important}.pr-8:not(table),.pr-8:not(.btn)>tbody>tr>td,.pr-8.btn td a,.px-8:not(table),.px-8:not(.btn)>tbody>tr>td,.px-8.btn td a{padding-right:32px !important}.pl-8:not(table),.pl-8:not(.btn)>tbody>tr>td,.pl-8.btn td a,.px-8:not(table),.px-8:not(.btn)>tbody>tr>td,.px-8.btn td a{padding-left:32px !important}*[class*=s-lg-]>tbody>tr>td{font-size:0 !important;line-height:0 !important;height:0 !important}.s-2>tbody>tr>td{font-size:8px !important;line-height:8px !important;height:8px !important}.s-6>tbody>tr>td{font-size:24px !important;line-height:24px !important;height:24px !important}.s-8>tbody>tr>td{font-size:32px !important;line-height:32px !important;height:32px !important}}
    </style>
  </head>
  <body class="bg-gray-100" style="outline: 0; width: 100%; min-width: 100%; height: 100%; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family: Helvetica, Arial, sans-serif; line-height: 24px; font-weight: normal; font-size: 16px; -moz-box-sizing: border-box; -webkit-box-sizing: border-box; box-sizing: border-box; color: #000000; margin: 0; padding: 0; border-width: 0;" bgcolor="#f7fafc">
    <table class="bg-gray-100 body" valign="top" role="presentation" border="0" cellpadding="0" cellspacing="0" style="outline: 0; width: 100%; min-width: 100%; height: 100%; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family: Helvetica, Arial, sans-serif; line-height: 24px; font-weight: normal; font-size: 16px; -moz-box-sizing: border-box; -webkit-box-sizing: border-box; box-sizing: border-box; color: #000000; margin: 0; padding: 0; border-width: 0;" bgcolor="#f7fafc">
      <tbody>
        <tr>
          <td valign="top" style="line-height: 24px; font-size: 16px; margin: 0;" align="left" bgcolor="#f7fafc">
            <table class="s-8 w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%;" width="100%">
              <tbody>
                <tr>
                  <td style="line-height: 32px; font-size: 32px; width: 100%; height: 32px; margin: 0;" align="left" width="100%" height="32">
                    &#160;
                  </td>
                </tr>
              </tbody>
            </table>
            <table class="max-w-2xl mx-auto  bg-white rounded-lg shadow-md overflow-hidden w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="border-radius: 8px; width: 100%;" bgcolor="#ffffff" width="100%">
              <tbody>
                <tr>
                  <td style="line-height: 24px; font-size: 16px; border-radius: 8px; width: 100%; margin: 0;" align="left" bgcolor="#ffffff" width="100%">
                    <table class="bg-indigo-600 py-6 px-8 w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%;" bgcolor="#520dc2" width="100%">
                      <tbody>
                        <tr>
                          <td style="line-height: 24px; font-size: 16px; width: 100%; margin: 0; padding: 24px 32px;" align="left" bgcolor="#520dc2" width="100%">
                            <h1 class="text-3xl font-bold text-white text-center" style="color: #ffffff; padding-top: 0; padding-bottom: 0; font-weight: 500; vertical-align: baseline; font-size: 30px; line-height: 36px; margin: 0;" align="center">Your OTP Code</h1>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                    <table class="p-8" role="presentation" border="0" cellpadding="0" cellspacing="0">
                      <tbody>
                        <tr>
                          <td style="line-height: 24px; font-size: 16px; margin: 0; padding: 32px;" align="left">
                            <div class="">
                              <p class="text-gray-700" style="line-height: 24px; font-size: 16px; color: #4a5568; width: 100%; margin: 0;" align="left">Hello,</p>
                              <table class="s-6 w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%;" width="100%">
                                <tbody>
                                  <tr>
                                    <td style="line-height: 24px; font-size: 24px; width: 100%; height: 24px; margin: 0;" align="left" width="100%" height="24">
                                      &#160;
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                              <p class="text-gray-700" style="line-height: 24px; font-size: 16px; color: #4a5568; width: 100%; margin: 0;" align="left">Your One-Time Password (OTP) for account verification is:</p>
                              <table class="s-6 w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%;" width="100%">
                                <tbody>
                                  <tr>
                                    <td style="line-height: 24px; font-size: 24px; width: 100%; height: 24px; margin: 0;" align="left" width="100%" height="24">
                                      &#160;
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                              <table class="bg-gray-100 rounded-lg p-4  w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="border-radius: 8px; width: 100%;" bgcolor="#f7fafc" width="100%">
                                <tbody>
                                  <tr>
                                    <td style="line-height: 24px; font-size: 16px; border-radius: 8px; width: 100%; margin: 0; padding: 16px;" align="left" bgcolor="#f7fafc" width="100%">
                                      <p class="text-4xl font-bold text-center text-indigo-600" style="line-height: 43.2px; font-size: 36px; color: #520dc2; width: 100%; margin: 0;" align="center">[otp]</p>
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                              <table class="s-6 w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%;" width="100%">
                                <tbody>
                                  <tr>
                                    <td style="line-height: 24px; font-size: 24px; width: 100%; height: 24px; margin: 0;" align="left" width="100%" height="24">
                                      &#160;
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                              <p class="text-gray-700" style="line-height: 24px; font-size: 16px; color: #4a5568; width: 100%; margin: 0;" align="left">This OTP is valid for <span class="font-semibold">8 hours</span>. Please do not share this code with anyone.</p>
                              <table class="s-6 w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%;" width="100%">
                                <tbody>
                                  <tr>
                                    <td style="line-height: 24px; font-size: 24px; width: 100%; height: 24px; margin: 0;" align="left" width="100%" height="24">
                                      &#160;
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                              <p class="text-gray-700" style="line-height: 24px; font-size: 16px; color: #4a5568; width: 100%; margin: 0;" align="left">If you didn't request this code, please ignore this email.</p>
                              <table class="s-2 w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%;" width="100%">
                                <tbody>
                                  <tr>
                                    <td style="line-height: 8px; font-size: 8px; width: 100%; height: 8px; margin: 0;" align="left" width="100%" height="8">
                                      &#160;
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                              <p class="text-gray-700" style="line-height: 24px; font-size: 16px; color: #4a5568; width: 100%; margin: 0;" align="left">Thank you for using our service!</p>
                            </div>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                    <table class="bg-gray-100 py-4 px-8 w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%;" bgcolor="#f7fafc" width="100%">
                      <tbody>
                        <tr>
                          <td style="line-height: 24px; font-size: 16px; width: 100%; margin: 0; padding: 16px 32px;" align="left" bgcolor="#f7fafc" width="100%">
                            <p class="text-sm text-gray-600 text-center" style="line-height: 16.8px; font-size: 14px; color: #718096; width: 100%; margin: 0;" align="center">&#169; 2025 jemaerp. All rights reserved.</p>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </td>
                </tr>
              </tbody>
            </table>
            <table class="s-8 w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%;" width="100%">
              <tbody>
                <tr>
                  <td style="line-height: 32px; font-size: 32px; width: 100%; height: 32px; margin: 0;" align="left" width="100%" height="32">
                    &#160;
                  </td>
                </tr>
              </tbody>
            </table>
          </td>
        </tr>
      </tbody>
    </table>
  </body>
</html>
        """
        return self.replace_tags(message, **kwargs)

    def send_org_created_email(self, **kwargs):
        message = \
        """
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html lang="en">
  <head>
    <!-- Compiled with Bootstrap Email version: 1.5.1 --><meta http-equiv="x-ua-compatible" content="ie=edge">
    <meta name="x-apple-disable-message-reformatting">
    <meta name="format-detection" content="telephone=no, date=no, address=no, email=no">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registration Was Successful</title>
    <style type="text/css">
      body,table,td{font-family:Helvetica,Arial,sans-serif !important}.ExternalClass{width:100%}.ExternalClass,.ExternalClass p,.ExternalClass span,.ExternalClass font,.ExternalClass td,.ExternalClass div{line-height:150%}a{text-decoration:none}*{color:inherit}a[x-apple-data-detectors],u+#body a,#MessageViewBody a{color:inherit;text-decoration:none;font-size:inherit;font-family:inherit;font-weight:inherit;line-height:inherit}img{-ms-interpolation-mode:bicubic}table:not([class^=s-]){font-family:Helvetica,Arial,sans-serif;mso-table-lspace:0pt;mso-table-rspace:0pt;border-spacing:0px;border-collapse:collapse}table:not([class^=s-]) td{border-spacing:0px;border-collapse:collapse}@media screen and (max-width: 600px){.w-full,.w-full>tbody>tr>td{width:100% !important}.p-4:not(table),.p-4:not(.btn)>tbody>tr>td,.p-4.btn td a{padding:16px !important}.pt-4:not(table),.pt-4:not(.btn)>tbody>tr>td,.pt-4.btn td a,.py-4:not(table),.py-4:not(.btn)>tbody>tr>td,.py-4.btn td a{padding-top:16px !important}.pb-4:not(table),.pb-4:not(.btn)>tbody>tr>td,.pb-4.btn td a,.py-4:not(table),.py-4:not(.btn)>tbody>tr>td,.py-4.btn td a{padding-bottom:16px !important}.pt-6:not(table),.pt-6:not(.btn)>tbody>tr>td,.pt-6.btn td a,.py-6:not(table),.py-6:not(.btn)>tbody>tr>td,.py-6.btn td a{padding-top:24px !important}.pb-6:not(table),.pb-6:not(.btn)>tbody>tr>td,.pb-6.btn td a,.py-6:not(table),.py-6:not(.btn)>tbody>tr>td,.py-6.btn td a{padding-bottom:24px !important}.p-8:not(table),.p-8:not(.btn)>tbody>tr>td,.p-8.btn td a{padding:32px !important}.pr-8:not(table),.pr-8:not(.btn)>tbody>tr>td,.pr-8.btn td a,.px-8:not(table),.px-8:not(.btn)>tbody>tr>td,.px-8.btn td a{padding-right:32px !important}.pl-8:not(table),.pl-8:not(.btn)>tbody>tr>td,.pl-8.btn td a,.px-8:not(table),.px-8:not(.btn)>tbody>tr>td,.px-8.btn td a{padding-left:32px !important}*[class*=s-lg-]>tbody>tr>td{font-size:0 !important;line-height:0 !important;height:0 !important}.s-2>tbody>tr>td{font-size:8px !important;line-height:8px !important;height:8px !important}.s-6>tbody>tr>td{font-size:24px !important;line-height:24px !important;height:24px !important}.s-8>tbody>tr>td{font-size:32px !important;line-height:32px !important;height:32px !important}}
    </style>
  </head>
  <body class="bg-gray-100" style="outline: 0; width: 100%; min-width: 100%; height: 100%; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family: Helvetica, Arial, sans-serif; line-height: 24px; font-weight: normal; font-size: 16px; -moz-box-sizing: border-box; -webkit-box-sizing: border-box; box-sizing: border-box; color: #000000; margin: 0; padding: 0; border-width: 0;" bgcolor="#f7fafc">
    <table class="bg-gray-100 body" valign="top" role="presentation" border="0" cellpadding="0" cellspacing="0" style="outline: 0; width: 100%; min-width: 100%; height: 100%; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family: Helvetica, Arial, sans-serif; line-height: 24px; font-weight: normal; font-size: 16px; -moz-box-sizing: border-box; -webkit-box-sizing: border-box; box-sizing: border-box; color: #000000; margin: 0; padding: 0; border-width: 0;" bgcolor="#f7fafc">
      <tbody>
        <tr>
          <td valign="top" style="line-height: 24px; font-size: 16px; margin: 0;" align="left" bgcolor="#f7fafc">
            <table class="s-8 w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%;" width="100%">
              <tbody>
                <tr>
                  <td style="line-height: 32px; font-size: 32px; width: 100%; height: 32px; margin: 0;" align="left" width="100%" height="32">
                    &#160;
                  </td>
                </tr>
              </tbody>
            </table>
            <table class="max-w-2xl mx-auto  bg-white rounded-lg shadow-md overflow-hidden w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="border-radius: 8px; width: 100%;" bgcolor="#ffffff" width="100%">
              <tbody>
                <tr>
                  <td style="line-height: 24px; font-size: 16px; border-radius: 8px; width: 100%; margin: 0;" align="left" bgcolor="#ffffff" width="100%">
                    <table class="bg-indigo-600 py-6 px-8 w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%;" bgcolor="#520dc2" width="100%">
                      <tbody>
                        <tr>
                          <td style="line-height: 24px; font-size: 16px; width: 100%; margin: 0; padding: 24px 32px;" align="left" bgcolor="#520dc2" width="100%">
                            <h1 class="text-3xl font-bold text-white text-center" style="color: #ffffff; padding-top: 0; padding-bottom: 0; font-weight: 500; vertical-align: baseline; font-size: 30px; line-height: 36px; margin: 0;" align="center">Welcome to JemaErp</h1>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                    <table class="p-8" role="presentation" border="0" cellpadding="0" cellspacing="0">
                      <tbody>
                        <tr>
                          <td style="line-height: 24px; font-size: 16px; margin: 0; padding: 32px;" align="left">
                            <div class="">
                              <p class="text-gray-700" style="line-height: 24px; font-size: 16px; color: #4a5568; width: 100%; margin: 0;" align="left">Dear [organisation],</p>
                              <table class="s-6 w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%;" width="100%">
                                <tbody>
                                  <tr>
                                    <td style="line-height: 24px; font-size: 24px; width: 100%; height: 24px; margin: 0;" align="left" width="100%" height="24">
                                      &#160;
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                              <p class="text-gray-700" style="line-height: 24px; font-size: 16px; color: #4a5568; width: 100%; margin: 0;" align="left">Hello, Welcome to <strong>JemaERP</strong>!</p>
                              <table class="s-6 w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%;" width="100%">
                                <tbody>
                                  <tr>
                                    <td style="line-height: 24px; font-size: 24px; width: 100%; height: 24px; margin: 0;" align="left" width="100%" height="24">
                                      &#160;
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                              <table class="s-6 w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%;" width="100%">
                                <tbody>
                                  <tr>
                                    <td style="line-height: 24px; font-size: 24px; width: 100%; height: 24px; margin: 0;" align="left" width="100%" height="24">
                                      &#160;
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                              <p class="text-gray-700" style="line-height: 24px; font-size: 16px; color: #4a5568; width: 100%; margin: 0;" align="left">We are currently reviewing your application and will get back to you within <strong>24 to 48 hours</strong>.</p>
                              <table class="s-6 w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%;" width="100%">
                                <tbody>
                                  <tr>
                                    <td style="line-height: 24px; font-size: 24px; width: 100%; height: 24px; margin: 0;" align="left" width="100%" height="24">
                                      &#160;
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                              <p class="text-gray-700" style="line-height: 24px; font-size: 16px; color: #4a5568; width: 100%; margin: 0;" align="left">If you didn't request this code, please ignore this email.</p>
                              <table class="s-2 w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%;" width="100%">
                                <tbody>
                                  <tr>
                                    <td style="line-height: 8px; font-size: 8px; width: 100%; height: 8px; margin: 0;" align="left" width="100%" height="8">
                                      &#160;
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                              <p class="text-gray-700" style="line-height: 24px; font-size: 16px; color: #4a5568; width: 100%; margin: 0;" align="left">Thank you for using our service!</p>
                            </div>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                    <table class="bg-gray-100 py-4 px-8 w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%;" bgcolor="#f7fafc" width="100%">
                      <tbody>
                        <tr>
                          <td style="line-height: 24px; font-size: 16px; width: 100%; margin: 0; padding: 16px 32px;" align="left" bgcolor="#f7fafc" width="100%">
                            <p class="text-sm text-gray-600 text-center" style="line-height: 16.8px; font-size: 14px; color: #718096; width: 100%; margin: 0;" align="center">&#169; 2025 jemaerp. All rights reserved.</p>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </td>
                </tr>
              </tbody>
            </table>
            <table class="s-8 w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%;" width="100%">
              <tbody>
                <tr>
                  <td style="line-height: 32px; font-size: 32px; width: 100%; height: 32px; margin: 0;" align="left" width="100%" height="32">
                    &#160;
                  </td>
                </tr>
              </tbody>
            </table>
          </td>
        </tr>
      </tbody>
    </table>
  </body>
</html>
        """
        return self.replace_tags(message, **kwargs)

    def send_approved_email(self, **kwargs):
        message = \
        """
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html lang="en" style="color: inherit;">
  <head>
    <!-- Compiled with Bootstrap Email version: 1.5.1 -->
    <!-- Compiled with Bootstrap Email version: 1.5.1 -->
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <meta name="x-apple-disable-message-reformatting">
    <meta name="format-detection" content="telephone=no, date=no, address=no, email=no">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Organization Approval Notification</title>
    <style>
      @media screen and (max-width: 600px) {
        .w-full {
          width: 100% !important;
        }
        .w-full>tbody>tr>td {
          width: 100% !important;
        }
        .p-4:not(table) {
          padding: 16px !important;
        }
        .p-4:not(.btn)>tbody>tr>td {
          padding: 16px !important;
        }
        .p-4.btn td a {
          padding: 16px !important;
        }
        .pt-4:not(table) {
          padding-top: 16px !important;
        }
        .pt-4:not(.btn)>tbody>tr>td {
          padding-top: 16px !important;
        }
        .pt-4.btn td a {
          padding-top: 16px !important;
        }
        .py-4:not(table) {
          padding-top: 16px !important;
        }
        .py-4:not(.btn)>tbody>tr>td {
          padding-top: 16px !important;
        }
        .py-4.btn td a {
          padding-top: 16px !important;
        }
        .pb-4:not(table) {
          padding-bottom: 16px !important;
        }
        .pb-4:not(.btn)>tbody>tr>td {
          padding-bottom: 16px !important;
        }
        .pb-4.btn td a {
          padding-bottom: 16px !important;
        }
        .py-4:not(table) {
          padding-bottom: 16px !important;
        }
        .py-4:not(.btn)>tbody>tr>td {
          padding-bottom: 16px !important;
        }
        .py-4.btn td a {
          padding-bottom: 16px !important;
        }
        .pt-6:not(table) {
          padding-top: 24px !important;
        }
        .pt-6:not(.btn)>tbody>tr>td {
          padding-top: 24px !important;
        }
        .pt-6.btn td a {
          padding-top: 24px !important;
        }
        .py-6:not(table) {
          padding-top: 24px !important;
        }
        .py-6:not(.btn)>tbody>tr>td {
          padding-top: 24px !important;
        }
        .py-6.btn td a {
          padding-top: 24px !important;
        }
        .pb-6:not(table) {
          padding-bottom: 24px !important;
        }
        .pb-6:not(.btn)>tbody>tr>td {
          padding-bottom: 24px !important;
        }
        .pb-6.btn td a {
          padding-bottom: 24px !important;
        }
        .py-6:not(table) {
          padding-bottom: 24px !important;
        }
        .py-6:not(.btn)>tbody>tr>td {
          padding-bottom: 24px !important;
        }
        .py-6.btn td a {
          padding-bottom: 24px !important;
        }
        .p-8:not(table) {
          padding: 32px !important;
        }
        .p-8:not(.btn)>tbody>tr>td {
          padding: 32px !important;
        }
        .p-8.btn td a {
          padding: 32px !important;
        }
        .pr-8:not(table) {
          padding-right: 32px !important;
        }
        .pr-8:not(.btn)>tbody>tr>td {
          padding-right: 32px !important;
        }
        .pr-8.btn td a {
          padding-right: 32px !important;
        }
        .px-8:not(table) {
          padding-right: 32px !important;
        }
        .px-8:not(.btn)>tbody>tr>td {
          padding-right: 32px !important;
        }
        .px-8.btn td a {
          padding-right: 32px !important;
        }
        .pl-8:not(table) {
          padding-left: 32px !important;
        }
        .pl-8:not(.btn)>tbody>tr>td {
          padding-left: 32px !important;
        }
        .pl-8.btn td a {
          padding-left: 32px !important;
        }
        .px-8:not(table) {
          padding-left: 32px !important;
        }
        .px-8:not(.btn)>tbody>tr>td {
          padding-left: 32px !important;
        }
        .px-8.btn td a {
          padding-left: 32px !important;
        }
        *[class*=s-lg-]>tbody>tr>td {
          font-size: 0 !important; line-height: 0 !important; height: 0 !important;
        }
        .s-2>tbody>tr>td {
          font-size: 8px !important; line-height: 8px !important; height: 8px !important;
        }
        .s-6>tbody>tr>td {
          font-size: 24px !important; line-height: 24px !important; height: 24px !important;
        }
        .s-8>tbody>tr>td {
          font-size: 32px !important; line-height: 32px !important; height: 32px !important;
        }
      }
    </style>          <style type="text/css">
      body,table,td{font-family:Helvetica,Arial,sans-serif !important}.ExternalClass{width:100%}.ExternalClass,.ExternalClass p,.ExternalClass span,.ExternalClass font,.ExternalClass td,.ExternalClass div{line-height:150%}a{text-decoration:none}*{color:inherit}a[x-apple-data-detectors],u+#body a,#MessageViewBody a{color:inherit;text-decoration:none;font-size:inherit;font-family:inherit;font-weight:inherit;line-height:inherit}img{-ms-interpolation-mode:bicubic}table:not([class^=s-]){font-family:Helvetica,Arial,sans-serif;mso-table-lspace:0pt;mso-table-rspace:0pt;border-spacing:0px;border-collapse:collapse}table:not([class^=s-]) td{border-spacing:0px;border-collapse:collapse}@media screen and (max-width: 600px){.w-full,.w-full>tbody>tr>td{width:100% !important}.pt-4:not(table),.pt-4:not(.btn)>tbody>tr>td,.pt-4.btn td a,.py-4:not(table),.py-4:not(.btn)>tbody>tr>td,.py-4.btn td a{padding-top:16px !important}.pb-4:not(table),.pb-4:not(.btn)>tbody>tr>td,.pb-4.btn td a,.py-4:not(table),.py-4:not(.btn)>tbody>tr>td,.py-4.btn td a{padding-bottom:16px !important}.pt-6:not(table),.pt-6:not(.btn)>tbody>tr>td,.pt-6.btn td a,.py-6:not(table),.py-6:not(.btn)>tbody>tr>td,.py-6.btn td a{padding-top:24px !important}.pb-6:not(table),.pb-6:not(.btn)>tbody>tr>td,.pb-6.btn td a,.py-6:not(table),.py-6:not(.btn)>tbody>tr>td,.py-6.btn td a{padding-bottom:24px !important}.p-8:not(table),.p-8:not(.btn)>tbody>tr>td,.p-8.btn td a{padding:32px !important}.pr-8:not(table),.pr-8:not(.btn)>tbody>tr>td,.pr-8.btn td a,.px-8:not(table),.px-8:not(.btn)>tbody>tr>td,.px-8.btn td a{padding-right:32px !important}.pl-8:not(table),.pl-8:not(.btn)>tbody>tr>td,.pl-8.btn td a,.px-8:not(table),.px-8:not(.btn)>tbody>tr>td,.px-8.btn td a{padding-left:32px !important}*[class*=s-lg-]>tbody>tr>td{font-size:0 !important;line-height:0 !important;height:0 !important}.s-6>tbody>tr>td{font-size:24px !important;line-height:24px !important;height:24px !important}.s-8>tbody>tr>td{font-size:32px !important;line-height:32px !important;height:32px !important}}
    </style>
  </head>
  <body class="bg-gray-100" style="outline: 0; width: 100%; min-width: 100%; height: 100%; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family: Helvetica,Arial,sans-serif !important; line-height: 24px; font-size: 16px; box-sizing: border-box; color: #000000; font-weight: normal; -moz-box-sizing: border-box; -webkit-box-sizing: border-box; margin: 0; padding: 0; border-width: 0;" bgcolor="#f7fafc">
    <table class="bg-gray-100 body" valign="top" role="presentation" border="0" cellpadding="0" cellspacing="0" style="outline: 0; width: 100%; min-width: 100%; height: 100%; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family: Helvetica,Arial,sans-serif !important; line-height: 24px; font-weight: normal; font-size: 16px; -moz-box-sizing: border-box; -webkit-box-sizing: border-box; box-sizing: border-box; color: #000000; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-spacing: 0px; border-collapse: collapse; margin: 0; padding: 0; border-width: 0;" bgcolor="#f7fafc">
      <tbody style="color: inherit;">
        <tr style="color: inherit;">
          <td valign="top" style="line-height: 24px; font-size: 16px; font-family: Helvetica,Arial,sans-serif !important; color: inherit; border-spacing: 0px; border-collapse: collapse; margin: 0;" align="left" bgcolor="#f7fafc">
            <table class="bg-gray-100 body" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%; min-width: 100%; height: 100%; font-family: Helvetica,Arial,sans-serif !important; line-height: 24px; font-size: 16px; box-sizing: border-box; color: #000000; outline: 0; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-weight: normal; -moz-box-sizing: border-box; -webkit-box-sizing: border-box; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-spacing: 0px; border-collapse: collapse; margin: 0; padding: 0; border-width: 0;" bgcolor="#f7fafc">
              <tbody style="color: inherit;">
                <tr style="color: inherit;">
                  <td valign="top" align="left" style="line-height: 24px; font-size: 16px; font-family: Helvetica,Arial,sans-serif !important; color: inherit; border-spacing: 0px; border-collapse: collapse; margin: 0;" bgcolor="#f7fafc">
                    <table class="s-8 w-full w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%; font-family: Helvetica,Arial,sans-serif !important; color: inherit;" width="100%">
                      <tbody style="color: inherit;">
                        <tr style="color: inherit;">
                          <td style="line-height: 32px; font-size: 32px; width: 100%; height: 32px; font-family: Helvetica,Arial,sans-serif !important; color: inherit; border-spacing: 0px; border-collapse: collapse; margin: 0;" align="left" width="100%" height="32">
                            &#160;
                          </td>
                        </tr>
                      </tbody>
                    </table>
                    <table class="max-w-2xl mx-auto bg-white rounded-lg shadow-md overflow-hidden w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="border-radius: 8px; width: 100%; font-family: Helvetica,Arial,sans-serif !important; color: inherit; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-spacing: 0px; border-collapse: collapse;" bgcolor="#ffffff" width="100%">
                      <tbody style="color: inherit;">
                        <tr style="color: inherit;">
                          <td align="left" bgcolor="#ffffff" style="line-height: 24px; font-size: 16px; border-radius: 8px; width: 100%; font-family: Helvetica,Arial,sans-serif !important; color: inherit; border-spacing: 0px; border-collapse: collapse; margin: 0;" width="100%">
                            <table class="bg-indigo-600 py-6 px-8 w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%; font-family: Helvetica,Arial,sans-serif !important; color: inherit; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-spacing: 0px; border-collapse: collapse;" bgcolor="#520dc2" width="100%">
                              <tbody style="color: inherit;">
                                <tr style="color: inherit;">
                                  <td align="left" bgcolor="#520dc2" style="line-height: 24px; font-size: 16px; width: 100%; font-family: Helvetica,Arial,sans-serif !important; color: inherit; border-spacing: 0px; border-collapse: collapse; margin: 0; padding: 24px 32px;" width="100%">
                                    <h1 class="text-3xl font-bold text-white text-center" style="color: #ffffff; font-weight: 500; vertical-align: baseline; font-size: 30px; line-height: 36px; margin: 0; padding: 0;" align="center">
                                      Organization Approval Notification
                                    </h1>
                                  </td>
                                </tr>
                              </tbody>
                            </table>
                            <table class="p-8" role="presentation" border="0" cellpadding="0" cellspacing="0" style="font-family: Helvetica,Arial,sans-serif !important; color: inherit; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-spacing: 0px; border-collapse: collapse;">
                              <tbody style="color: inherit;">
                                <tr style="color: inherit;">
                                  <td align="left" style="line-height: 24px; font-size: 16px; font-family: Helvetica,Arial,sans-serif !important; color: inherit; border-spacing: 0px; border-collapse: collapse; margin: 0; padding: 32px;">
                                    <div style="color: inherit;">
                                      <p class="text-gray-700" style="line-height: 24px; font-size: 16px; color: #4a5568; width: 100%; margin: 0;" align="left">
                                        Dear [organization_name],
                                      </p>
                                      <table class="s-6 w-full w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%; font-family: Helvetica,Arial,sans-serif !important; color: inherit;" width="100%">
                                        <tbody style="color: inherit;">
                                          <tr style="color: inherit;">
                                            <td style="line-height: 24px; font-size: 24px; width: 100%; height: 24px; font-family: Helvetica,Arial,sans-serif !important; color: inherit; border-spacing: 0px; border-collapse: collapse; margin: 0;" align="left" width="100%" height="24">
                                              &#160;
                                            </td>
                                          </tr>
                                        </tbody>
                                      </table>
                                      <p class="text-gray-700" style="line-height: 24px; font-size: 16px; color: #4a5568; width: 100%; margin: 0;" align="left">
                                        Your organisation has been approved.
                                      </p>
                                      <table class="s-6 w-full w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%; font-family: Helvetica,Arial,sans-serif !important; color: inherit;" width="100%">
                                        <tbody style="color: inherit;">
                                          <tr style="color: inherit;">
                                            <td style="line-height: 24px; font-size: 24px; width: 100%; height: 24px; font-family: Helvetica,Arial,sans-serif !important; color: inherit; border-spacing: 0px; border-collapse: collapse; margin: 0;" align="left" width="100%" height="24">
                                              &#160;
                                            </td>
                                          </tr>
                                        </tbody>
                                      </table>
                                      <p class="text-gray-700" style="line-height: 24px; font-size: 16px; color: #4a5568; width: 100%; margin: 0;" align="left">
                                        Your admin credentials are as follows:
                                      </p>
                                      <table class="s-6 w-full w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%; font-family: Helvetica,Arial,sans-serif !important; color: inherit;" width="100%">
                                        <tbody style="color: inherit;">
                                          <tr style="color: inherit;">
                                            <td style="line-height: 24px; font-size: 24px; width: 100%; height: 24px; font-family: Helvetica,Arial,sans-serif !important; color: inherit; border-spacing: 0px; border-collapse: collapse; margin: 0;" align="left" width="100%" height="24">
                                              &#160;
                                            </td>
                                          </tr>
                                        </tbody>
                                      </table>
                                      <p class="text-gray-700" style="line-height: 24px; font-size: 16px; color: #4a5568; width: 100%; margin: 0;" align="left">
                                        Username: {username}<br style="color: inherit;">
                                        Password: {password}
                                      </p>
                                      <table class="s-6 w-full w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%; font-family: Helvetica,Arial,sans-serif !important; color: inherit;" width="100%">
                                        <tbody style="color: inherit;">
                                          <tr style="color: inherit;">
                                            <td style="line-height: 24px; font-size: 24px; width: 100%; height: 24px; font-family: Helvetica,Arial,sans-serif !important; color: inherit; border-spacing: 0px; border-collapse: collapse; margin: 0;" align="left" width="100%" height="24">
                                              &#160;
                                            </td>
                                          </tr>
                                        </tbody>
                                      </table>
                                      <p class="text-gray-700" style="line-height: 24px; font-size: 16px; color: #4a5568; width: 100%; margin: 0;" align="left">
                                        Please change your password upon first login.
                                      </p>
                                    </div>
                                  </td>
                                </tr>
                              </tbody>
                            </table>
                            <table class="bg-gray-100 py-4 px-8 w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%; font-family: Helvetica,Arial,sans-serif !important; color: inherit; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-spacing: 0px; border-collapse: collapse;" bgcolor="#f7fafc" width="100%">
                              <tbody style="color: inherit;">
                                <tr style="color: inherit;">
                                  <td align="left" bgcolor="#f7fafc" style="line-height: 24px; font-size: 16px; width: 100%; font-family: Helvetica,Arial,sans-serif !important; color: inherit; border-spacing: 0px; border-collapse: collapse; margin: 0; padding: 16px 32px;" width="100%">
                                    <p class="text-sm text-gray-600 text-center" style="line-height: 16.8px; font-size: 14px; color: #718096; width: 100%; margin: 0;" align="center">
                                      &#169; 2025 jemaerp. All rights reserved.
                                    </p>
                                  </td>
                                </tr>
                              </tbody>
                            </table>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                    <table class="s-8 w-full w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%; font-family: Helvetica,Arial,sans-serif !important; color: inherit;" width="100%">
                      <tbody style="color: inherit;">
                        <tr style="color: inherit;">
                          <td style="line-height: 32px; font-size: 32px; width: 100%; height: 32px; font-family: Helvetica,Arial,sans-serif !important; color: inherit; border-spacing: 0px; border-collapse: collapse; margin: 0;" align="left" width="100%" height="32">
                            &#160;
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </td>
                </tr>
              </tbody>
            </table>
          </td>
        </tr>
      </tbody>
    </table>
  </body>
</html>

        """
        return self.replace_tags(message, **kwargs)

    def rejection_email(self, **kwargs):
        message = \
        """
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html lang="en" style="color: inherit;">
  <head>
    <!-- Compiled with Bootstrap Email version: 1.5.1 -->
    <!-- Compiled with Bootstrap Email version: 1.5.1 -->
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <meta name="x-apple-disable-message-reformatting">
    <meta name="format-detection" content="telephone=no, date=no, address=no, email=no">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Organization Application Rejection Notification</title>
    <style>
      @media screen and (max-width: 600px) {
        .w-full {
          width: 100% !important;
        }
        .w-full>tbody>tr>td {
          width: 100% !important;
        }
        .p-4:not(table) {
          padding: 16px !important;
        }
        .p-4:not(.btn)>tbody>tr>td {
          padding: 16px !important;
        }
        .p-4.btn td a {
          padding: 16px !important;
        }
        .pt-4:not(table) {
          padding-top: 16px !important;
        }
        .pt-4:not(.btn)>tbody>tr>td {
          padding-top: 16px !important;
        }
        .pt-4.btn td a {
          padding-top: 16px !important;
        }
        .py-4:not(table) {
          padding-top: 16px !important;
        }
        .py-4:not(.btn)>tbody>tr>td {
          padding-top: 16px !important;
        }
        .py-4.btn td a {
          padding-top: 16px !important;
        }
        .pb-4:not(table) {
          padding-bottom: 16px !important;
        }
        .pb-4:not(.btn)>tbody>tr>td {
          padding-bottom: 16px !important;
        }
        .pb-4.btn td a {
          padding-bottom: 16px !important;
        }
        .py-4:not(table) {
          padding-bottom: 16px !important;
        }
        .py-4:not(.btn)>tbody>tr>td {
          padding-bottom: 16px !important;
        }
        .py-4.btn td a {
          padding-bottom: 16px !important;
        }
        .pt-6:not(table) {
          padding-top: 24px !important;
        }
        .pt-6:not(.btn)>tbody>tr>td {
          padding-top: 24px !important;
        }
        .pt-6.btn td a {
          padding-top: 24px !important;
        }
        .py-6:not(table) {
          padding-top: 24px !important;
        }
        .py-6:not(.btn)>tbody>tr>td {
          padding-top: 24px !important;
        }
        .py-6.btn td a {
          padding-top: 24px !important;
        }
        .pb-6:not(table) {
          padding-bottom: 24px !important;
        }
        .pb-6:not(.btn)>tbody>tr>td {
          padding-bottom: 24px !important;
        }
        .pb-6.btn td a {
          padding-bottom: 24px !important;
        }
        .py-6:not(table) {
          padding-bottom: 24px !important;
        }
        .py-6:not(.btn)>tbody>tr>td {
          padding-bottom: 24px !important;
        }
        .py-6.btn td a {
          padding-bottom: 24px !important;
        }
        .p-8:not(table) {
          padding: 32px !important;
        }
        .p-8:not(.btn)>tbody>tr>td {
          padding: 32px !important;
        }
        .p-8.btn td a {
          padding: 32px !important;
        }
        .pr-8:not(table) {
          padding-right: 32px !important;
        }
        .pr-8:not(.btn)>tbody>tr>td {
          padding-right: 32px !important;
        }
        .pr-8.btn td a {
          padding-right: 32px !important;
        }
        .px-8:not(table) {
          padding-right: 32px !important;
        }
        .px-8:not(.btn)>tbody>tr>td {
          padding-right: 32px !important;
        }
        .px-8.btn td a {
          padding-right: 32px !important;
        }
        .pl-8:not(table) {
          padding-left: 32px !important;
        }
        .pl-8:not(.btn)>tbody>tr>td {
          padding-left: 32px !important;
        }
        .pl-8.btn td a {
          padding-left: 32px !important;
        }
        .px-8:not(table) {
          padding-left: 32px !important;
        }
        .px-8:not(.btn)>tbody>tr>td {
          padding-left: 32px !important;
        }
        .px-8.btn td a {
          padding-left: 32px !important;
        }
        *[class*=s-lg-]>tbody>tr>td {
          font-size: 0 !important; line-height: 0 !important; height: 0 !important;
        }
        .s-2>tbody>tr>td {
          font-size: 8px !important; line-height: 8px !important; height: 8px !important;
        }
        .s-6>tbody>tr>td {
          font-size: 24px !important; line-height: 24px !important; height: 24px !important;
        }
        .s-8>tbody>tr>td {
          font-size: 32px !important; line-height: 32px !important; height: 32px !important;
        }
      }
    </style>          <style type="text/css">
      body,table,td{font-family:Helvetica,Arial,sans-serif !important}.ExternalClass{width:100%}.ExternalClass,.ExternalClass p,.ExternalClass span,.ExternalClass font,.ExternalClass td,.ExternalClass div{line-height:150%}a{text-decoration:none}*{color:inherit}a[x-apple-data-detectors],u+#body a,#MessageViewBody a{color:inherit;text-decoration:none;font-size:inherit;font-family:inherit;font-weight:inherit;line-height:inherit}img{-ms-interpolation-mode:bicubic}table:not([class^=s-]){font-family:Helvetica,Arial,sans-serif;mso-table-lspace:0pt;mso-table-rspace:0pt;border-spacing:0px;border-collapse:collapse}table:not([class^=s-]) td{border-spacing:0px;border-collapse:collapse}@media screen and (max-width: 600px){.w-full,.w-full>tbody>tr>td{width:100% !important}.pt-4:not(table),.pt-4:not(.btn)>tbody>tr>td,.pt-4.btn td a,.py-4:not(table),.py-4:not(.btn)>tbody>tr>td,.py-4.btn td a{padding-top:16px !important}.pb-4:not(table),.pb-4:not(.btn)>tbody>tr>td,.pb-4.btn td a,.py-4:not(table),.py-4:not(.btn)>tbody>tr>td,.py-4.btn td a{padding-bottom:16px !important}.pt-6:not(table),.pt-6:not(.btn)>tbody>tr>td,.pt-6.btn td a,.py-6:not(table),.py-6:not(.btn)>tbody>tr>td,.py-6.btn td a{padding-top:24px !important}.pb-6:not(table),.pb-6:not(.btn)>tbody>tr>td,.pb-6.btn td a,.py-6:not(table),.py-6:not(.btn)>tbody>tr>td,.py-6.btn td a{padding-bottom:24px !important}.p-8:not(table),.p-8:not(.btn)>tbody>tr>td,.p-8.btn td a{padding:32px !important}.pr-8:not(table),.pr-8:not(.btn)>tbody>tr>td,.pr-8.btn td a,.px-8:not(table),.px-8:not(.btn)>tbody>tr>td,.px-8.btn td a{padding-right:32px !important}.pl-8:not(table),.pl-8:not(.btn)>tbody>tr>td,.pl-8.btn td a,.px-8:not(table),.px-8:not(.btn)>tbody>tr>td,.px-8.btn td a{padding-left:32px !important}*[class*=s-lg-]>tbody>tr>td{font-size:0 !important;line-height:0 !important;height:0 !important}.s-6>tbody>tr>td{font-size:24px !important;line-height:24px !important;height:24px !important}.s-8>tbody>tr>td{font-size:32px !important;line-height:32px !important;height:32px !important}}
    </style>
  </head>
  <body class="bg-gray-100" style="outline: 0; width: 100%; min-width: 100%; height: 100%; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family: Helvetica, Arial, sans-serif !important; line-height: 24px; font-size: 16px; box-sizing: border-box; color: #000000; font-weight: normal; -moz-box-sizing: border-box; -webkit-box-sizing: border-box; margin: 0; padding: 0; border-width: 0;" bgcolor="#f7fafc">
    <table class="bg-gray-100 body" valign="top" role="presentation" border="0" cellpadding="0" cellspacing="0" style="outline: 0; width: 100%; min-width: 100%; height: 100%; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family: Helvetica, Arial, sans-serif !important; line-height: 24px; font-weight: normal; font-size: 16px; -moz-box-sizing: border-box; -webkit-box-sizing: border-box; box-sizing: border-box; color: #000000; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-spacing: 0px; border-collapse: collapse; margin: 0; padding: 0; border-width: 0;" bgcolor="#f7fafc">
      <tbody style="color: inherit;">
        <tr style="color: inherit;">
          <td valign="top" style="line-height: 24px; font-size: 16px; font-family: Helvetica, Arial, sans-serif !important; color: inherit; border-spacing: 0px; border-collapse: collapse; margin: 0;" align="left" bgcolor="#f7fafc">
            <table class="bg-gray-100 body" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%; min-width: 100%; height: 100%; font-family: Helvetica, Arial, sans-serif !important; line-height: 24px; font-size: 16px; box-sizing: border-box; color: #000000; outline: 0; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-weight: normal; -moz-box-sizing: border-box; -webkit-box-sizing: border-box; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-spacing: 0px; border-collapse: collapse; margin: 0; padding: 0; border-width: 0;" bgcolor="#f7fafc">
              <tbody style="color: inherit;">
                <tr style="color: inherit;">
                  <td valign="top" align="left" style="line-height: 24px; font-size: 16px; font-family: Helvetica, Arial, sans-serif !important; color: inherit; border-spacing: 0px; border-collapse: collapse; margin: 0;" bgcolor="#f7fafc">
                    <table class="s-8 w-full w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%; font-family: Helvetica, Arial, sans-serif !important; color: inherit;" width="100%">
                      <tbody style="color: inherit;">
                        <tr style="color: inherit;">
                          <td style="line-height: 32px; font-size: 32px; width: 100%; height: 32px; font-family: Helvetica, Arial, sans-serif !important; color: inherit; border-spacing: 0px; border-collapse: collapse; margin: 0;" align="left" width="100%" height="32">
                            &#160;
                          </td>
                        </tr>
                      </tbody>
                    </table>
                    <table class="max-w-2xl mx-auto bg-white rounded-lg shadow-md overflow-hidden w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="border-radius: 8px; width: 100%; font-family: Helvetica, Arial, sans-serif !important; color: inherit; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-spacing: 0px; border-collapse: collapse;" bgcolor="#ffffff" width="100%">
                      <tbody style="color: inherit;">
                        <tr style="color: inherit;">
                          <td align="left" bgcolor="#ffffff" style="line-height: 24px; font-size: 16px; border-radius: 8px; width: 100%; font-family: Helvetica, Arial, sans-serif !important; color: inherit; border-spacing: 0px; border-collapse: collapse; margin: 0;" width="100%">
                            <table class="bg-indigo-600 py-6 px-8 w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%; font-family: Helvetica, Arial, sans-serif !important; color: inherit; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-spacing: 0px; border-collapse: collapse;" bgcolor="#520dc2" width="100%">
                              <tbody style="color: inherit;">
                                <tr style="color: inherit;">
                                  <td align="left" bgcolor="#520dc2" style="line-height: 24px; font-size: 16px; width: 100%; font-family: Helvetica, Arial, sans-serif !important; color: inherit; border-spacing: 0px; border-collapse: collapse; margin: 0; padding: 24px 32px;" width="100%">
                                    <h1 class="text-3xl font-bold text-white text-center" style="color: #ffffff; font-weight: 500; vertical-align: baseline; font-size: 30px; line-height: 36px; margin: 0; padding: 0;" align="center">
                                      Organization Application Rejection Notification
                                    </h1>
                                  </td>
                                </tr>
                              </tbody>
                            </table>
                            <table class="p-8" role="presentation" border="0" cellpadding="0" cellspacing="0" style="font-family: Helvetica, Arial, sans-serif !important; color: inherit; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-spacing: 0px; border-collapse: collapse;">
                              <tbody style="color: inherit;">
                                <tr style="color: inherit;">
                                  <td align="left" style="line-height: 24px; font-size: 16px; font-family: Helvetica, Arial, sans-serif !important; color: inherit; border-spacing: 0px; border-collapse: collapse; margin: 0; padding: 32px;">
                                    <div style="color: inherit;">
                                      <p class="text-gray-700" style="line-height: 24px; font-size: 16px; color: #4a5568; width: 100%; margin: 0;" align="left">
                                        Dear {organization_name},
                                      </p>
                                      <table class="s-6 w-full w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%; font-family: Helvetica, Arial, sans-serif !important; color: inherit;" width="100%">
                                        <tbody style="color: inherit;">
                                          <tr style="color: inherit;">
                                            <td style="line-height: 24px; font-size: 24px; width: 100%; height: 24px; font-family: Helvetica, Arial, sans-serif !important; color: inherit; border-spacing: 0px; border-collapse: collapse; margin: 0;" align="left" width="100%" height="24">
                                              &#160;
                                            </td>
                                          </tr>
                                        </tbody>
                                      </table>
                                      <p class="text-gray-700" style="line-height: 24px; font-size: 16px; color: #4a5568; width: 100%; margin: 0;" align="left">
                                        We regret to inform you that your organisation application has been rejected.
                                      </p>
                                    </div>
                                  </td>
                                </tr>
                              </tbody>
                            </table>
                            <table class="bg-gray-100 py-4 px-8 w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%; font-family: Helvetica, Arial, sans-serif !important; color: inherit; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-spacing: 0px; border-collapse: collapse;" bgcolor="#f7fafc" width="100%">
                              <tbody style="color: inherit;">
                                <tr style="color: inherit;">
                                  <td align="left" bgcolor="#f7fafc" style="line-height: 24px; font-size: 16px; width: 100%; font-family: Helvetica, Arial, sans-serif !important; color: inherit; border-spacing: 0px; border-collapse: collapse; margin: 0; padding: 16px 32px;" width="100%">
                                    <p class="text-sm text-gray-600 text-center" style="line-height: 16.8px; font-size: 14px; color: #718096; width: 100%; margin: 0;" align="center">
                                      &#169; 2025 jemaerp. All rights reserved.
                                    </p>
                                  </td>
                                </tr>
                              </tbody>
                            </table>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                    <table class="s-8 w-full w-full" role="presentation" border="0" cellpadding="0" cellspacing="0" style="width: 100%; font-family: Helvetica, Arial, sans-serif !important; color: inherit;" width="100%">
                      <tbody style="color: inherit;">
                        <tr style="color: inherit;">
                          <td style="line-height: 32px; font-size: 32px; width: 100%; height: 32px; font-family: Helvetica, Arial, sans-serif !important; color: inherit; border-spacing: 0px; border-collapse: collapse; margin: 0;" align="left" width="100%" height="32">
                            &#160;
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </td>
                </tr>
              </tbody>
            </table>
          </td>
        </tr>
      </tbody>
    </table>
  </body>
</html>

        """
        return self.replace_tags(message, **kwargs)