from django.db import models
from django.utils import timezone
import json
import os

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_published = models.DateTimeField(default=timezone.now)

    
    # Your model fields here

    @staticmethod
    def get_all_posts():
        # Construct the file path using BASE_DIR
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, 'data', 'blog_posts.json')
        print(f"File path: {file_path}")  # Add this line
        try:
            with open('C:\\Users\\hrran\\Desktop\\json_blog_project\\data\\blog_posts.json', 'r') as json_file:
                posts = json.load(json_file)
        except Exception as e:
            # Print the exception to understand the issue
            print(f"Error loading JSON file: {e}")
            posts = []

        return posts


    
    def __str__(self):
        return self.title