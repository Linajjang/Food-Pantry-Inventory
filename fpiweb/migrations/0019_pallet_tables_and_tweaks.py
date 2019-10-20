# Generated by Django 2.2.5 on 2019-10-19 20:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fpiweb', '0018_profile_active_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pallet',
            fields=[
                ('id', models.AutoField(help_text='Internal record identifier for a pallet.', primary_key=True, serialize=False, verbose_name='Internal Pallet ID')),
                ('pallet_status', models.CharField(choices=[('Fill', 'Fill pallet for new location'), ('Merge', 'Merging boxes on pallet'), ('Move', 'Moving boxes to new location')], help_text='Current status of pallet.', max_length=15, verbose_name='Pallet Status')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Pallets',
                'ordering': ['user'],
            },
        ),
        migrations.AlterModelOptions(
            name='productexample',
            options={'ordering': ['prod_example_name'], 'verbose_name_plural': 'Product Examples'},
        ),
        migrations.RenameField(
            model_name='productexample',
            old_name='prod_id',
            new_name='product',
        ),
        migrations.AddField(
            model_name='activity',
            name='adjustment_code',
            field=models.CharField(blank=True, choices=[('Add Emptied', 'Add emptied previous contents'), ('Move Added', 'Move added box'), ('Consume Added', 'Consume added box')], help_text='Coded reason if this entry was adjusted', max_length=15, null=True, verbose_name='Adjustment Code'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='date_consumed',
            field=models.DateField(blank=True, help_text='Date product was consumed.', null=True, verbose_name='Date Box Emptied'),
        ),
        migrations.AlterField(
            model_name='locbin',
            name='loc_bin_descr',
            field=models.CharField(help_text='Location bin description', max_length=20, verbose_name='Loc Bin Description'),
        ),
        migrations.AlterField(
            model_name='locrow',
            name='loc_row_descr',
            field=models.CharField(help_text='Location row description', max_length=20, verbose_name='Loc Row Description'),
        ),
        migrations.AlterField(
            model_name='loctier',
            name='loc_tier_descr',
            field=models.CharField(help_text='Location tier description', max_length=20, verbose_name='Loc Tier Description'),
        ),
        migrations.CreateModel(
            name='PalletBox',
            fields=[
                ('id', models.AutoField(help_text='Internal record identifier for a pallet box.', primary_key=True, serialize=False, verbose_name='Internal Pallet Box ID')),
                ('box_number', models.CharField(help_text='Number printed in the label on the box.', max_length=8, unique=True, verbose_name='Visible Box Number')),
                ('exp_year', models.IntegerField(help_text='Year the product expires, if filled.', verbose_name='Year Product Expires')),
                ('exp_month_start', models.IntegerField(blank=True, help_text='Optional starting month range of when the product expires, if filled.', null=True, verbose_name='Expiration Start Month (Optional)')),
                ('exp_month_end', models.IntegerField(blank=True, help_text='Optional ending month range of when the product expires, if filled.', null=True, verbose_name='Expiration End Month (Optional)')),
                ('box_status', models.CharField(choices=[('New', 'New box added'), ('Original', 'Box already here'), ('Move', 'Box being moved')], help_text='Box on pallet status.', max_length=15, verbose_name='Box Status')),
                ('box', models.ForeignKey(help_text='Internal record identifier for a box.', on_delete=django.db.models.deletion.PROTECT, to='fpiweb.Box')),
                ('pallet', models.ForeignKey(help_text='Internal record identifier for a pallet.', on_delete=django.db.models.deletion.PROTECT, to='fpiweb.Pallet')),
                ('product', models.ForeignKey(help_text='Product contained in this box, if filled.', on_delete=django.db.models.deletion.PROTECT, to='fpiweb.Product', verbose_name='product')),
            ],
            options={
                'verbose_name_plural': 'Pallet Boxes',
                'ordering': '',
            },
        ),
        migrations.AddField(
            model_name='pallet',
            name='pallet_loc_bin',
            field=models.ForeignKey(help_text='Target bin for this pallet', on_delete=django.db.models.deletion.PROTECT, to='fpiweb.LocBin', verbose_name='Bin'),
        ),
        migrations.AddField(
            model_name='pallet',
            name='pallet_loc_row',
            field=models.ForeignKey(help_text='Target row for this pallet', on_delete=django.db.models.deletion.PROTECT, to='fpiweb.LocRow', verbose_name='Row'),
        ),
        migrations.AddField(
            model_name='pallet',
            name='pallet_loc_tier',
            field=models.ForeignKey(help_text='Target bin for this pallet', on_delete=django.db.models.deletion.PROTECT, to='fpiweb.LocTier', verbose_name='Tier'),
        ),
        migrations.AlterField(
            model_name='pallet',
            name='user',
            field=models.OneToOneField(help_text='User managing this pallet', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='productexample',
            name='id',
            field=models.AutoField(help_text='Internal record identifier for product example', primary_key=True, serialize=False, verbose_name='Internal Product Example ID'),
        ),
    ]
