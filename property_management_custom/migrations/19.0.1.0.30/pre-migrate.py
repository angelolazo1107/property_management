import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    """Clean drop stale FK columns across crm_lead, sale_order, lease_contract, property_reservation, tenant_application_bis."""
    try:
        cr.execute("ALTER TABLE crm_lead DROP COLUMN IF EXISTS target_unit_id CASCADE;")
        cr.execute("ALTER TABLE crm_lead DROP COLUMN IF EXISTS target_property_id CASCADE;")
        cr.execute("ALTER TABLE crm_lead DROP COLUMN IF EXISTS building_id CASCADE;")
        cr.execute("ALTER TABLE sale_order DROP COLUMN IF EXISTS target_unit_id CASCADE;")
        cr.execute("ALTER TABLE property_reservation DROP COLUMN IF EXISTS unit_id CASCADE;")
        cr.execute("ALTER TABLE tenant_application_bis DROP COLUMN IF EXISTS unit_id CASCADE;")
        cr.execute("ALTER TABLE lease_contract DROP COLUMN IF EXISTS unit_id CASCADE;")
        _logger.info("Migration 19.0.1.0.30: cleanly dropped unit_id and building_id columns")
    except Exception as e:
        _logger.warning("Migration 19.0.1.0.30 error: %s", e)
