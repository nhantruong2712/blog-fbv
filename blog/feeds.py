from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed

from blog.models import Post


class BlogFeed(Feed):
	title = "Nhandz's Blog"
	link = "/blog"
	description = "Hacking, Tricks, and more"

	def items(self):
		return Post.visible_posts.all()[:20]

	def items_title(self, item):
		return item.title

	def item_description(self, item):
		return item.preview().replace('\r\n', ' ')


class BlogAtomFeed(BlogFeed):
	feed_type = Atom1Feed
	subtitle = BlogFeed.description
