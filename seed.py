from models import db, Pet
from app import app

# Create all tables
db.drop_all()
db.create_all()

Pet.query.delete()

coco = Pet(name='Coco', species="dog", photo_url="https://th.bing.com/th/id/OIP.r4hbAo1SgaXg5XQlck4FOAHaEA?w=335&h=181&c=7&o=5&pid=1.7", age=2)
blacky = Pet(name='Blacky', species="dog", photo_url="https://buzzsharer.com/wp-content/uploads/2015/04/Black-puppy-lab.jpg", age=3)
snugglepuff = Pet(name='Snugglepuff', species="pufferfish", photo_url="https://aquariumfish.net/images_01/puffer_090430_w0480.jpg", age=2)
comet = Pet(name='Comet', species="hyacinth macaw", photo_url="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Anodorhynchus_hyacinthinus_-Disney_-Florida-8.jpg/800px-Anodorhynchus_hyacinthinus_-Disney_-Florida-8.jpg", age=2)


db.session.add_all([coco, blacky, snugglepuff, comet])
db.session.commit()