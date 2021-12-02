letter = """
    Dear {salutation} {name}

    Thank you for your letter. We are sorry that our {product} {verbed} in your
{room}. Please note that it should never be used in a {room}, especially near any 
{animals}.

    Send us your receipt and {amount} for shipping and handling. We will send you
another {product} that, in our tests, is {percent}% less likely to have {verbed}.

    Thank you for your support.
    Sincerely,
    {spokesman}
    {job_title}
"""
print(
    letter.format(
        salutation="Ambassador",
        name="Nibbler",
        product="pudding",
        verbed="evaporated",
        room="gazebo",
        animals="octothorpes",
        amount="$1.99",
        percent=88,
        spokesman="Shirley Iugeste",
        job_title="I Hate This job",
    )
)
