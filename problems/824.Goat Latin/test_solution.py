from solution import Solution


def test_solution():
    sentence = "I speak Goat Latin"
    expected = "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
    result = Solution().toGoatLatin(sentence)
    assert expected == result

    # sentence = "The quick brown fox jumped over the lazy dog"
    # expected = "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
    # result = Solution().toGoatLatin(sentence)
    # assert expected == result
