from django import forms


class HotelFilterForm(forms.Form):
    price_min = forms.IntegerField(label='min-price', required=False)
    price_max = forms.IntegerField(label='max-price', required=False)

    ordering_price = forms.ChoiceField(label='сортировка', required=False, choices=[
        ['price_min', 'ПО ЦЕНЕ'],
    ])

    ordering_model = forms.ChoiceField(label='сортировка', required=False, choices=[
        ['model_hostel', 'ПО ТИПУ'],
    ])

    ordering_rating = forms.ChoiceField(label='сортировка', required=False, choices=[
        ['rating', 'ПО РЕЙТИНГУ'],
    ])

    ordering = forms.ChoiceField(label='сортировка', required=False, choices=[
        ['price_min', 'ПО ЦЕНЕ'],
        ['model_hostel', 'ПО ТИПУ'],
        ['rating', 'ПО РЕЙТИНГУ'],
    ])
    #
    # model_hostel = forms.ChoiceField(label='модель', required=False, choices=[
    #     ['АПАРТАМЕНТЫ', 'АПАРТАМЕНТЫ'],
    #     ['ГОСТИНИЦА', 'ГОСТИНИЦА'],
    #     ['МОТЕЛЬ', 'МОТЕЛЬ'],
    # ])
