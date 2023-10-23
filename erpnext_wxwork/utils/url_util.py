import frappe
from urllib.parse import quote, urlparse


def get_domain():
    """
    获取域名
    :return:
    """
    return (frappe.get_conf().domain or frappe.local.site)


def append_domain(url):
    """
    拼接域名
    :param url:
    :return:
    """
    return get_domain() + url


def append_domain_protocol(url):
    """
    拼接http+域名
    :param url:
    :return:
    """

    domain = get_domain()
    if "http" not in domain:
        domain = "http://" + domain
    return domain + url


def wxwork_oauth_url(url):
    """
    企业微信授权链接
    :param url:
    :return:
    """
    url = quote(append_domain(url))
    return append_domain("/api/method/erpnext_wxwork.oauth.redirect?url=" + url)
