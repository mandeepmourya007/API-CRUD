from rest_framework import serializers
from . models import student

class studentSerializer(serializers.ModelSerializer):
    
    
    size = serializers.SerializerMethodField('get_size')

    def get_size(self, student):
        return  len(student.name)
    class Meta:
        model = student
        fields = ["rollno","name","size"]
    
    
    