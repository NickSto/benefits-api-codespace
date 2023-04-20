from screener.models import Screen, HouseholdMember, IncomeStream, Expense, Message
from rest_framework import serializers
from programs.serializers import NavigatorSerializer


class MessageSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Message
        fields = '__all__'


class IncomeStreamSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = IncomeStream
        fields = '__all__'
        read_only_fields = ('screen', 'household_member', 'id')


class ExpenseSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Expense
        fields = '__all__'
        read_only_fields = ('screen', 'household_member', 'id')


class HouseholdMemberSerializer(serializers.ModelSerializer):
    income_streams = IncomeStreamSerializer(many=True)

    class Meta:
        model = HouseholdMember
        fields = (
            'id',
            'screen',
            'relationship',
            'age',
            'student',
            'student_full_time',
            'pregnant',
            'unemployed',
            'worked_in_last_18_mos',
            'visually_impaired',
            'disabled',
            'veteran',
            'medicaid',
            'disability_medicaid',
            'has_income',
            'income_streams'
        )
        read_only_fields = ('screen', 'id')


class ScreenSerializer(serializers.ModelSerializer):
    household_members = HouseholdMemberSerializer(many=True)
    expenses = ExpenseSerializer(many=True)

    class Meta:
        model = Screen
        fields = (
            'id',
            'uuid',
            'is_test',
            'start_date',
            'submission_date',
            'agree_to_tos',
            'zipcode',
            'county',
            'referral_source',
            'referrer_code',
            'household_size',
            'household_assets',
            'housing_situation',
            'household_members',
            'last_email_request_date',
            'last_tax_filing_year',
            'expenses',
            'user',
            'external_id',
            'request_language_code',
            'has_tanf',
            'has_wic',
            'has_snap',
            'has_lifeline',
            'has_acp',
            'has_eitc',
            'has_coeitc',
            'has_nslp',
            'has_ctc',
            'has_medicaid',
            'has_rtdlive',
            'has_cccap',
            'has_mydenver',
            'has_chp',
            'has_ccb',
            'has_ssi',
            'has_employer_hi',
            'has_private_hi',
            'has_medicaid_hi',
            'has_medicare_hi',
            'has_chp_hi',
            'has_no_hi',
            'needs_food',
            'needs_baby_supplies',
            'needs_housing_help',
            'needs_mental_health_help',
            'needs_child_dev_help',
            'needs_funeral_help',
            'needs_family_planning_help'
        )
        read_only_fields = ('id', 'uuid', 'submision_date', 'last_email_request_date')
        create_only_fields = ('user', 'start_date')

    def create(self, validated_data):
        household_members = validated_data.pop('household_members')
        expenses = validated_data.pop('expenses')
        screen = Screen.objects.create(**validated_data)
        for member in household_members:
            incomes = member.pop('income_streams')
            household_member = HouseholdMember.objects.create(**member, screen=screen)
            for income in incomes:
                IncomeStream.objects.create(**income, screen=screen, household_member=household_member)
        for expense in expenses:
            Expense.objects.create(**expense, screen=screen)
        return screen

    def update(self, instance, validated_data):
        household_members = validated_data.pop('household_members')
        expenses = validated_data.pop('expenses')
        Screen.objects.filter(pk=instance.id).update(**validated_data)
        HouseholdMember.objects.filter(screen=instance).delete()
        Expense.objects.filter(screen=instance).delete()
        for member in household_members:
            incomes = member.pop('income_streams')
            household_member = HouseholdMember.objects.create(**member, screen=instance)
            for income in incomes:
                IncomeStream.objects.create(**income, screen=instance, household_member=household_member)
        for expense in expenses:
            Expense.objects.create(**expense, screen=instance)
        return instance


class EligibilitySerializer(serializers.Serializer):
    description_short = serializers.CharField()
    name = serializers.CharField()
    name_abbreviated = serializers.CharField()
    description = serializers.CharField()
    value_type = serializers.CharField()
    learn_more_link = serializers.CharField()
    apply_button_link = serializers.CharField()
    estimated_value = serializers.IntegerField()
    estimated_delivery_time = serializers.CharField()
    estimated_application_time = serializers.CharField()
    legal_status_required = serializers.CharField()
    category = serializers.CharField()
    eligible = serializers.BooleanField()
    failed_tests = serializers.ListField()
    passed_tests = serializers.ListField()
    estimated_value = serializers.IntegerField()
    navigators = NavigatorSerializer(many=True)
    already_has = serializers.BooleanField()
    new = serializers.BooleanField()

    class Meta:
        fields = '__all__'


class EligibilityTranslationSerializer(serializers.Serializer):
    translations = serializers.DictField()

    class Meta:
        fields = ('translations',)
