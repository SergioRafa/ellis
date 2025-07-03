    # Código a ser executado quando a aplicação estiver finalizando (opcional)

app = FastAPI(
    title="API de Gestão Escolar",
    description="Permite realizar diferentes operações em cada uma dessas entidades.",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(alunos_router, tags=["alunos"])
app.include_router(cursos_router, tags=["cursos"])
app.include_router(matriculas_router, tags=["matrículas"])

