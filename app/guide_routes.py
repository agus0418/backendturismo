from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.forms import GuideForm
from app.models import Guide

bp = Blueprint('guide', __name__)

@bp.route('/guides')
@login_required
def index():
    guides = Guide.query.all()
    return render_template('guides/index.html', guides=guides)

@bp.route('/guides/create', methods=['GET', 'POST'])
@login_required
def create():
    if not current_user.can_manage_guides:
        return redirect(url_for('main.index'))
    form = GuideForm()
    if form.validate_on_submit():
        guide = Guide(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            dni=form.dni.data,
            city=form.city.data,
            province=form.province.data,
            activities=form.activities.data
        )
        db.session.add(guide)
        db.session.commit()
        flash('Guide created successfully.')
        return redirect(url_for('guide.index'))
    return render_template('guides/create_guide.html', form=form)

@bp.route('/guides/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    if not current_user.can_manage_guides:
        return redirect(url_for('main.index'))
    guide = Guide.query.get_or_404(id)
    form = GuideForm(obj=guide)
    if form.validate_on_submit():
        guide.first_name = form.first_name.data
        guide.last_name = form.last_name.data
        guide.dni = form.dni.data
        guide.city = form.city.data
        guide.province = form.province.data
        guide.activities = form.activities.data
        db.session.commit()
        flash('Guide updated successfully.')
        return redirect(url_for('guide.index'))
    return render_template('guides/edit_guide.html', form=form, guide=guide)

@bp.route('/guides/delete/<int:id>', methods=['POST'])
@login_required
def delete(id):
    if not current_user.can_manage_guides:
        return redirect(url_for('main.index'))
    guide = Guide.query.get_or_404(id)
    db.session.delete(guide)
    db.session.commit()
    flash('Guide deleted successfully.')
    return redirect(url_for('guide.index'))
