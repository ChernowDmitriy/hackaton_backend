"""initialMigrate

Revision ID: adef5a4367f2
Revises: 
Create Date: 2024-06-16 13:31:25.646073

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'adef5a4367f2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address_register_of_real_estate_objects',
    sa.Column('useless_id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('global_id', sa.BIGINT(), nullable=True),
    sa.Column('obj_type', sa.String(), nullable=True),
    sa.Column('OnTerritoryOfMoscow', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('unom', sa.BIGINT(), nullable=True),
    sa.Column('P1', sa.String(), nullable=True),
    sa.Column('P3', sa.String(), nullable=True),
    sa.Column('P4', sa.String(), nullable=True),
    sa.Column('P5', sa.String(), nullable=True),
    sa.Column('P6', sa.String(), nullable=True),
    sa.Column('P7', sa.String(), nullable=True),
    sa.Column('P90', sa.String(), nullable=True),
    sa.Column('simple_address', sa.String(), nullable=True),
    sa.Column('P91', sa.String(), nullable=True),
    sa.Column('l1_type', sa.String(), nullable=True),
    sa.Column('l1_value', sa.String(), nullable=True),
    sa.Column('l2_type', sa.String(), nullable=True),
    sa.Column('p0', sa.String(), nullable=True),
    sa.Column('l2_value', sa.String(), nullable=True),
    sa.Column('l3_type', sa.String(), nullable=True),
    sa.Column('P2', sa.String(), nullable=True),
    sa.Column('l3_value', sa.String(), nullable=True),
    sa.Column('l4_type', sa.String(), nullable=True),
    sa.Column('l4_value', sa.String(), nullable=True),
    sa.Column('l5_type', sa.String(), nullable=True),
    sa.Column('l5_value', sa.String(), nullable=True),
    sa.Column('adm_area', sa.String(), nullable=True),
    sa.Column('district', sa.String(), nullable=True),
    sa.Column('nreg', sa.String(), nullable=True),
    sa.Column('dreg', sa.String(), nullable=True),
    sa.Column('n_fias', sa.String(), nullable=True),
    sa.Column('d_fias', sa.String(), nullable=True),
    sa.Column('kad_n', sa.String(), nullable=True),
    sa.Column('kad_zu', sa.String(), nullable=True),
    sa.Column('kladr', sa.String(), nullable=True),
    sa.Column('tdoc', sa.String(), nullable=True),
    sa.Column('ndoc', sa.String(), nullable=True),
    sa.Column('ddoc', sa.String(), nullable=True),
    sa.Column('adr_type', sa.String(), nullable=True),
    sa.Column('vid', sa.String(), nullable=True),
    sa.Column('sostad', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('geodata', sa.String(), nullable=True),
    sa.Column('geodata_center', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('useless_id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_address_register_of_real_estate_objects_useless_id'), 'address_register_of_real_estate_objects', ['useless_id'], unique=False, schema='public')
    op.create_table('addresses',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('unom', sa.BIGINT(), nullable=True),
    sa.Column('latitude', sa.String(), nullable=True),
    sa.Column('longitude', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_addresses_id'), 'addresses', ['id'], unique=False, schema='public')
    op.create_table('asupr_data_with_dispatch_dso_center',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('short_address', sa.String(), nullable=True),
    sa.Column('full_address', sa.String(), nullable=True),
    sa.Column('area', sa.String(), nullable=True),
    sa.Column('unom', sa.BIGINT(), nullable=True),
    sa.Column('group', sa.String(), nullable=True),
    sa.Column('ods_number', sa.String(), nullable=True),
    sa.Column('ods_address', sa.String(), nullable=True),
    sa.Column('consumer', sa.String(), nullable=True),
    sa.Column('ctp', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_asupr_data_with_dispatch_dso_center_id'), 'asupr_data_with_dispatch_dso_center', ['id'], unique=False, schema='public')
    op.create_table('bti_unloading',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('administrative_district', sa.String(), nullable=True),
    sa.Column('municipal_district', sa.String(), nullable=True),
    sa.Column('locality', sa.String(), nullable=True),
    sa.Column('street', sa.String(), nullable=True),
    sa.Column('house_type', sa.String(), nullable=True),
    sa.Column('house_numbers', sa.BIGINT(), nullable=True),
    sa.Column('housing_numbers', sa.BIGINT(), nullable=True),
    sa.Column('building_type_number', sa.String(), nullable=True),
    sa.Column('building_number', sa.String(), nullable=True),
    sa.Column('unom', sa.BIGINT(), nullable=True),
    sa.Column('unad', sa.BIGINT(), nullable=True),
    sa.Column('building_material', sa.String(), nullable=True),
    sa.Column('building_assignment', sa.String(), nullable=True),
    sa.Column('building_class', sa.String(), nullable=True),
    sa.Column('building_type', sa.String(), nullable=True),
    sa.Column('building_floors_number', sa.BIGINT(), nullable=True),
    sa.Column('building_attribute', sa.String(), nullable=True),
    sa.Column('building_total_area', sa.DOUBLE_PRECISION(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_bti_unloading_id'), 'bti_unloading', ['id'], unique=False, schema='public')
    op.create_table('economic_characteristics_houses',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('unom', sa.BIGINT(), nullable=True),
    sa.Column('district', sa.String(), nullable=True),
    sa.Column('area', sa.String(), nullable=True),
    sa.Column('col_758', sa.BIGINT(), nullable=True),
    sa.Column('col_759', sa.BIGINT(), nullable=True),
    sa.Column('col_760', sa.BIGINT(), nullable=True),
    sa.Column('col_761', sa.BIGINT(), nullable=True),
    sa.Column('col_762', sa.Float(), nullable=True),
    sa.Column('col_763', sa.Float(), nullable=True),
    sa.Column('col_764', sa.Float(), nullable=True),
    sa.Column('col_766', sa.BIGINT(), nullable=True),
    sa.Column('col_769', sa.BIGINT(), nullable=True),
    sa.Column('col_770', sa.BIGINT(), nullable=True),
    sa.Column('col_771', sa.BIGINT(), nullable=True),
    sa.Column('col_772', sa.BIGINT(), nullable=True),
    sa.Column('col_775', sa.BIGINT(), nullable=True),
    sa.Column('col_781', sa.BIGINT(), nullable=True),
    sa.Column('col_1945_del', sa.BIGINT(), nullable=True),
    sa.Column('col_2463', sa.BIGINT(), nullable=True),
    sa.Column('col_3163', sa.BIGINT(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_economic_characteristics_houses_id'), 'economic_characteristics_houses', ['id'], unique=False, schema='public')
    op.create_table('files',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('path', sa.String(), nullable=False),
    sa.Column('ext', sa.String(), nullable=False),
    sa.Column('byte_size', sa.BIGINT(), nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
    sa.Column('modify_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_files_id'), 'files', ['id'], unique=False, schema='public')
    op.create_table('incidents',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('source', sa.String(), nullable=True),
    sa.Column('external_system_creation_date', postgresql.TIMESTAMP(timezone=True), server_default=sa.text("TIMEZONE('utc', now())"), nullable=True),
    sa.Column('closed_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text("TIMEZONE('utc', now())"), nullable=True),
    sa.Column('area', sa.String(), nullable=True),
    sa.Column('unom', sa.BIGINT(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('external_system_closed_date', postgresql.TIMESTAMP(timezone=True), server_default=sa.text("TIMEZONE('utc', now())"), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_incidents_id'), 'incidents', ['id'], unique=False, schema='public')
    op.create_table('moek_wiring_diagrams',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('tp_number', sa.String(), nullable=True),
    sa.Column('address_tp', sa.String(), nullable=True),
    sa.Column('tp_type', sa.String(), nullable=True),
    sa.Column('placement_type', sa.String(), nullable=True),
    sa.Column('administrative_district', sa.String(), nullable=True),
    sa.Column('municipal_district', sa.String(), nullable=True),
    sa.Column('heat_supply_source', sa.String(), nullable=True),
    sa.Column('commissioning_date', postgresql.TIMESTAMP(timezone=True), server_default=sa.text("TIMEZONE('utc', now())"), nullable=True),
    sa.Column('balance_holder', sa.String(), nullable=True),
    sa.Column('building_street', sa.String(), nullable=True),
    sa.Column('heat_load_average', sa.DOUBLE_PRECISION(), nullable=True),
    sa.Column('heat_load_fact', sa.DOUBLE_PRECISION(), nullable=True),
    sa.Column('building_heat_load', sa.DOUBLE_PRECISION(), nullable=True),
    sa.Column('building_ventilation_heat_load', sa.DOUBLE_PRECISION(), nullable=True),
    sa.Column('is_dispatching', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_moek_wiring_diagrams_id'), 'moek_wiring_diagrams', ['id'], unique=False, schema='public')
    op.create_table('planned_unplanned_shutdowns',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('cause', sa.String(), nullable=True),
    sa.Column('source', sa.String(), nullable=True),
    sa.Column('registration_disconnection_date', postgresql.TIMESTAMP(timezone=True), server_default=sa.text("TIMEZONE('utc', now())"), nullable=True),
    sa.Column('planned_shutdown_date', postgresql.TIMESTAMP(timezone=True), server_default=sa.text("TIMEZONE('utc', now())"), nullable=True),
    sa.Column('planned_switch_on_date', postgresql.TIMESTAMP(timezone=True), server_default=sa.text("TIMEZONE('utc', now())"), nullable=True),
    sa.Column('actual_shutdown_date', postgresql.TIMESTAMP(timezone=True), server_default=sa.text("TIMEZONE('utc', now())"), nullable=True),
    sa.Column('actual_switch_on_date', postgresql.TIMESTAMP(timezone=True), server_default=sa.text("TIMEZONE('utc', now())"), nullable=True),
    sa.Column('shutdown_type', sa.String(), nullable=True),
    sa.Column('unom', sa.BIGINT(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_planned_unplanned_shutdowns_id'), 'planned_unplanned_shutdowns', ['id'], unique=False, schema='public')
    op.create_table('predictions',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('unom', sa.BIGINT(), nullable=True),
    sa.Column('district', sa.String(), nullable=True),
    sa.Column('building_material', sa.String(), nullable=True),
    sa.Column('building_assignment', sa.String(), nullable=True),
    sa.Column('building_total_area', sa.BIGINT(), nullable=True),
    sa.Column('area', sa.String(), nullable=True),
    sa.Column('project_number', sa.BIGINT(), nullable=True),
    sa.Column('floors_number', sa.BIGINT(), nullable=True),
    sa.Column('entrances_number', sa.BIGINT(), nullable=True),
    sa.Column('apartments_number', sa.BIGINT(), nullable=True),
    sa.Column('building_class', sa.String(), nullable=True),
    sa.Column('heat_supply_volume', sa.BIGINT(), nullable=True),
    sa.Column('heat_reverse_supply_volume', sa.BIGINT(), nullable=True),
    sa.Column('backflow_difference', sa.BIGINT(), nullable=True),
    sa.Column('leakage_difference', sa.BIGINT(), nullable=True),
    sa.Column('supply_temperature', sa.BIGINT(), nullable=True),
    sa.Column('return_temperature', sa.BIGINT(), nullable=True),
    sa.Column('counter_hours', sa.BIGINT(), nullable=True),
    sa.Column('heat_energy_consumption', sa.BIGINT(), nullable=True),
    sa.Column('municipal_district', sa.String(), nullable=True),
    sa.Column('emergency_status', sa.BIGINT(), nullable=True),
    sa.Column('total_area', sa.BIGINT(), nullable=True),
    sa.Column('total_area_lived_spaced', sa.BIGINT(), nullable=True),
    sa.Column('total_area_unlived_spaced', sa.BIGINT(), nullable=True),
    sa.Column('depreciation', sa.BIGINT(), nullable=True),
    sa.Column('wall_material', sa.BIGINT(), nullable=True),
    sa.Column('freight_elevators_number', sa.BIGINT(), nullable=True),
    sa.Column('housing_type', sa.BIGINT(), nullable=True),
    sa.Column('mkd_status', sa.BIGINT(), nullable=True),
    sa.Column('occurrence_year', sa.BIGINT(), nullable=True),
    sa.Column('occurrence_month', sa.BIGINT(), nullable=True),
    sa.Column('occurrence_day', sa.BIGINT(), nullable=True),
    sa.Column('predicted_label', sa.String(), nullable=True),
    sa.Column('elevators_number', sa.BIGINT(), nullable=True),
    sa.Column('prediction_title', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_predictions_id'), 'predictions', ['id'], unique=False, schema='public')
    op.create_table('social_facilities_efficiency_energies',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('building', sa.String(), nullable=True),
    sa.Column('count_buildings', sa.BIGINT(), nullable=True),
    sa.Column('total_area', sa.Float(), nullable=True),
    sa.Column('heated_area', sa.DOUBLE_PRECISION(), nullable=True),
    sa.Column('employees_average_number', sa.BIGINT(), nullable=True),
    sa.Column('building_type', sa.String(), nullable=True),
    sa.Column('energy_efficiency_class', sa.String(), nullable=True),
    sa.Column('floors_count', sa.BIGINT(), nullable=True),
    sa.Column('elevators_number', sa.BIGINT(), nullable=True),
    sa.Column('building_actual_depreciation', sa.BIGINT(), nullable=True),
    sa.Column('entrance_count', sa.BIGINT(), nullable=True),
    sa.Column('building_start_year', sa.BIGINT(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_social_facilities_efficiency_energies_id'), 'social_facilities_efficiency_energies', ['id'], unique=False, schema='public')
    op.create_table('unloading_odpu_heating',
    sa.Column('useless_id', sa.Uuid(), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('id_uu', sa.BIGINT(), nullable=True),
    sa.Column('id_tu', sa.BIGINT(), nullable=True),
    sa.Column('area', sa.String(), nullable=True),
    sa.Column('district', sa.String(), nullable=True),
    sa.Column('consumer', sa.String(), nullable=True),
    sa.Column('group', sa.String(), nullable=True),
    sa.Column('unom', sa.BIGINT(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('central_heating', sa.String(), nullable=True),
    sa.Column('meter_brand', sa.String(), nullable=True),
    sa.Column('series_number_meter', sa.BIGINT(), nullable=True),
    sa.Column('month_year', sa.String(), nullable=True),
    sa.Column('day_month_year', sa.String(), nullable=True),
    sa.Column('unit', sa.String(), nullable=True),
    sa.Column('heat_supply_volume', sa.DOUBLE_PRECISION(), nullable=True),
    sa.Column('heat_reverse_supply_volume', sa.DOUBLE_PRECISION(), nullable=True),
    sa.Column('backflow_difference', sa.DOUBLE_PRECISION(), nullable=True),
    sa.Column('leakage_difference', sa.DOUBLE_PRECISION(), nullable=True),
    sa.Column('supply_temperature', sa.DOUBLE_PRECISION(), nullable=True),
    sa.Column('return_temperature', sa.DOUBLE_PRECISION(), nullable=True),
    sa.Column('counter_hours', sa.DOUBLE_PRECISION(), nullable=True),
    sa.Column('heat_energy_consumption', sa.DOUBLE_PRECISION(), nullable=True),
    sa.Column('errors', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('useless_id', 'id_uu'),
    schema='public'
    )
    op.create_table('users',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('middle_name', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), server_default='True', nullable=False),
    sa.Column('refresh_token', sa.String(), nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
    sa.Column('modify_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_users_id'), 'users', ['id'], unique=False, schema='public')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_public_users_id'), table_name='users', schema='public')
    op.drop_table('users', schema='public')
    op.drop_table('unloading_odpu_heating', schema='public')
    op.drop_index(op.f('ix_public_social_facilities_efficiency_energies_id'), table_name='social_facilities_efficiency_energies', schema='public')
    op.drop_table('social_facilities_efficiency_energies', schema='public')
    op.drop_index(op.f('ix_public_predictions_id'), table_name='predictions', schema='public')
    op.drop_table('predictions', schema='public')
    op.drop_index(op.f('ix_public_planned_unplanned_shutdowns_id'), table_name='planned_unplanned_shutdowns', schema='public')
    op.drop_table('planned_unplanned_shutdowns', schema='public')
    op.drop_index(op.f('ix_public_moek_wiring_diagrams_id'), table_name='moek_wiring_diagrams', schema='public')
    op.drop_table('moek_wiring_diagrams', schema='public')
    op.drop_index(op.f('ix_public_incidents_id'), table_name='incidents', schema='public')
    op.drop_table('incidents', schema='public')
    op.drop_index(op.f('ix_public_files_id'), table_name='files', schema='public')
    op.drop_table('files', schema='public')
    op.drop_index(op.f('ix_public_economic_characteristics_houses_id'), table_name='economic_characteristics_houses', schema='public')
    op.drop_table('economic_characteristics_houses', schema='public')
    op.drop_index(op.f('ix_public_bti_unloading_id'), table_name='bti_unloading', schema='public')
    op.drop_table('bti_unloading', schema='public')
    op.drop_index(op.f('ix_public_asupr_data_with_dispatch_dso_center_id'), table_name='asupr_data_with_dispatch_dso_center', schema='public')
    op.drop_table('asupr_data_with_dispatch_dso_center', schema='public')
    op.drop_index(op.f('ix_public_addresses_id'), table_name='addresses', schema='public')
    op.drop_table('addresses', schema='public')
    op.drop_index(op.f('ix_public_address_register_of_real_estate_objects_useless_id'), table_name='address_register_of_real_estate_objects', schema='public')
    op.drop_table('address_register_of_real_estate_objects', schema='public')
    # ### end Alembic commands ###
