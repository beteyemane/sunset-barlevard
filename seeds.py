from app import app, db
from models.user import User, UserSchema
from models.bar import Bar, BarSchema
from models.crawl import Crawl, CrawlSchema, Stop, Comment, CommentSchema

user_schema = UserSchema()

with app.app_context():
    db.drop_all()
    db.create_all()

################ USERS ########################

    mike, errors = user_schema.load({
        'username': 'mike',
        'email': 'mike',
        'bio': 'Strange',
        'password': 'password',
        'password_confirmation': 'password'
    })

    if errors:
        raise Exception(errors)

    db.session.add(mike)

################ BARS ###############################

    jujus = Bar(
        name='Jujus',
        address='Ely\'s Yard, 15 Hanbury St, London E1 6QR',
        lat=51.520886,
        lng=-0.073487,
        terrace=True,
        description='We go all the time on Firdays',
        hero='https://www.abouttimemagazine.co.uk/wp-content/uploads/2017/05/IMG_22701.jpg',
        location='East'
    )
    db.session.add(jujus)

    the_culpeper = Bar(
        name='The Culpeper',
        address='40 Commercial St, London E1 6LP',
        lat=51.5168921,
        lng=-0.0730285,
        terrace=True,
        description='Small but great roofterrace',
        hero='https://www.theculpeper.com/wp-content/uploads/2015/11/Details_080.jpg',
        location='East'
    )
    db.session.add(the_culpeper)

    discount_suit_company = Bar(
        name='Discount Suit Company',
        address='29 Wentworth St, London E1 7TB',
        lat=51.5166773,
        lng=0.0774967,
        terrace=False,
        description='Basement no light',
        hero='http://london.lecool.com/files/2014/05/APR_DSC_INTERIOR_BAR-1024x780.jpg',
        location='East'
    )
    db.session.add(discount_suit_company)

    blind_beggar = Bar(
        name='The Blind Beggar',
        address='337 Whitechapel Rd, London E1 1BU',
        lat=51.3112,
        lng=0.0325,
        terrace=True,
        description='This famous pub is where Ronnie Kray murdered George Cornell in front of witnesses, and is the location of William Booth''s first sermon, which led to the creation of the Salvation Army. It was also the nearest outlet (or brewery tap) for the Manns Albion brewery, where the first modern Brown Ale was brewed',
        hero='https://www.traveldarkly.com/wp-content/uploads/2016/09/Kray-Twins-Gangsters-Blind-Beggar-Pub-Whitechapel-1030x687.jpg',
        location='East'
    )
    db.session.add(blind_beggar)

    pub_on_park = Bar(
        name='Pub on the Park',
        address='19 Martello St, London E8 3PE',
        lat=51.5166773,
        lng=0.0774967,
        terrace=True,
        description='Situated on the very edge of London Fields, "Pub on the Park" have spectacular views across the park, Summer or Winter, and are easily accessible from Hackney Central, London Fields or Haggerston overground and a multitude of buses.',
        hero='http://pubonthepark.com/wp-content/uploads/2016/11/Deck03.jpg',
        location='East'
    )
    db.session.add(pub_on_park)

    royal_oak = Bar(
        name='The Royal Oak',
        address='73 Columbia Rd, London E2 7RG',
        lat=51.5295,
        lng=0.0693,
        terrace=False,
        description='Situated on the very edge of London Fields, "Pub on the Park" have spectacular views across the park, Summer or Winter, and are easily accessible from Hackney Central, London Fields or Haggerston overground and a multitude of buses.',
        hero='https://static1.squarespace.com/static/59db5b973e00beb58c5bea65/t/5a46691df9619a146c44b184/1514563871674/39dac393c7f87544e94f805018ece333.jpg?format=2500w',
        location='East'
    )
    db.session.add(royal_oak)

################ CRAWLS ######################

    east_end = Crawl(
        name='East End Crawl',
        description='Tour of the seven wonders of the East End'
    )

    camden_crawl = Crawl(
        name='Camden Crawl',
        description='The best crawl ever!'
    )

    shoreditch_crawl = Crawl(
        name='Shoreditch Crawl',
        description='So much fun'
    )


############### STOPS ############################

    east_end.stops = [
        Stop(bar=blind_beggar, order=0),
        Stop(bar=royal_oak, order=1),
        Stop(bar=pub_on_park, order=2),
    ]
    db.session.add(east_end)

    camden_crawl.stops = [
        Stop(bar=blind_beggar, order=1),
        Stop(bar=royal_oak, order=0),
        Stop(bar=pub_on_park, order=2),
    ]
    db.session.add(camden_crawl)

    shoreditch_crawl.stops = [
        Stop(bar=blind_beggar, order=2),
        Stop(bar=royal_oak, order=1),
        Stop(bar=pub_on_park, order=0),
    ]
    db.session.add(shoreditch_crawl)

############## COMMENTS ###########################

    comment1 = Comment(content='Hate this crawl is dead rubbish', crawl=east_end)
    db.session.add(comment1)


    db.session.commit()
