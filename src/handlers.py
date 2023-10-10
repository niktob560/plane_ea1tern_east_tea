from typing import List

from aiohttp import web

from repo import PersonaRepo
from route import routes
from schema import PersonRequest
from schema import PersonResponse


@routes.get('/persons/{id}')
async def get_person_by_id(request: web.Request) -> PersonResponse:
    person_id = request.match_info['id']
    return PersonaRepo.find_by_id(person_id)


@routes.get('/persons')
async def get_persons(request: web.Request) -> List[PersonResponse]:
    return PersonaRepo.find()


@routes.post('/persons')
async def post_persons(request: web.Request):
    dat: dict = await request.json()
    person = PersonaRepo.create(PersonRequest.from_raw(dat))
    return web.Response(status=201, headers={'Location': f'/api/v1/persons/{person._id}'})


@routes.patch('/persons/{id}')
async def patch_persons(request: web.Request):
    dat = await request.json()
    person_id = int(request.match_info['id'])
    return PersonaRepo.patch(person_id, dat)


@routes.delete('/persons/{id}')
async def delete_persons(request: web.Request):
    person_id = request.match_info['id']
    PersonaRepo.delete(person_id)
    return web.Response(status=204)
