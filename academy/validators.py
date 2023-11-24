from rest_framework import serializers


class UrlValidator:
    def __call__(self, url):
        if not url.startswith('https://youtube.com'):
            raise serializers.ValidationError('You can save link only from youtube')

