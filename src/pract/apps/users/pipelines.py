import json
import urllib


def get_avatar(backend, strategy, details, response, user=None, *args, **kwargs):

    url = None
    if backend.name == 'facebook':
        url = "http://graph.facebook.com/%s/picture?type=large"%response['id']

    if backend.name == 'twitter':
        url = response.get('profile_image_url', '').replace('_normal','')

    if url:
        user.avatar = url
        user.save()


# def update_user_social_data(strategy, *args, **kwargs):
#     if not kwargs['is_new']:
#         return
#
#     user = kwargs['user']
#
#     fbuid = kwargs['response']['id']
#     access_token = kwargs['response']['access_token']
#
#     url = u'https://graph.facebook.com/{0}/' \
#           u'?fields=email' \
#           u'&access_token={1}'.format(
#         fbuid,
#         access_token,
#     )
#
#     request = urllib.Request(url)
#     email = json.loads(urllib.urlopen(request).read()).get('email')
#
#     user.email = email
#     user.save()