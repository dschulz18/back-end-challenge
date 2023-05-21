import graphene
from app.models import Person, Address


class AddressType(graphene.ObjectType):
    number = graphene.Int()
    street = graphene.String()
    city = graphene.String()
    state = graphene.String()

class PersonType(graphene.ObjectType):
    email = graphene.String()
    name = graphene.String()
    address = graphene.Field(AddressType)

class Query(graphene.ObjectType):
    people = graphene.List(PersonType)

    def resolve_people(self, info):
        return Person.objects.all()

class CreatePersonMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String()
        name = graphene.String()
        address_number = graphene.Int()
        address_street = graphene.String()
        address_city = graphene.String()
        address_state = graphene.String()

    person = graphene.Field(PersonType)

    @staticmethod
    def mutate(root, info, email, name, address_number, address_street, address_city, address_state):
        address = Address.objects.create(
            number=address_number,
            street=address_street,
            city=address_city,
            state=address_state
        )
        person = Person.objects.create(
            email=email,
            name=name,
            address=address
        )
        return CreatePersonMutation(person=person)

class Mutation(graphene.ObjectType):
    create_person = CreatePersonMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
