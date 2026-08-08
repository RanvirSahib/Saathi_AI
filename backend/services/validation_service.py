from backend.repositories.validation_repository import (
    save_validation
)


def log_validation(
    request,
    result
):

    if result["valid"]:

        save_validation(

            request,

            "SUCCESS",

            "Validated"

        )

    else:

        save_validation(

            request,

            "FAILED",

            ", ".join(result["errors"])

        )