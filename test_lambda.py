import lambda_function

def test_page_exists():
    response = lambda_function.lambda_handler({'key1': 'Kubernetes'}, "context")
    print(response)
    status = f'{response["statusCode"]}'
    content = f'{response["title"]}'
    print(content)
    expect_status = "200"
    expect_content = '"Kubernetes"'
    assert expect_status == status
    assert expect_content == content

def test_page_missing():
    response = lambda_function.lambda_handler({'key1': 'NonExistingPageWithStrangeName'}, "context")
    status = f'{response["statusCode"]}'
    expect = "400"
    assert expect == status

test_page_exists()